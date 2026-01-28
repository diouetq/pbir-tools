# -*- coding: utf-8 -*-
import os
import json
import copy

def pbir_duplicate_bookmark(
    pbir_folder_path,
    report_root_name,
    source_page_name="main",
    target_pages=None,
    bookmark_name=None
):
    """
    Duplique, modifie et synchronise (avec suppression) les bookmarks.
    """

    def safe_json_load(raw, path):
        if raw is None: return None
        try:
            return json.loads(raw.decode("utf-8") if isinstance(raw, bytes) else raw)
        except: return None

    # --- 1. Chargement des fichiers ---
    files_dict = {}
    for root, _, files in os.walk(pbir_folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, pbir_folder_path).replace("\\", "/")
            with open(full_path, "rb") as f:
                files_dict[rel_path] = f.read()

    pages_root = f"{report_root_name}/definition/pages/"
    bookmarks_root = f"{report_root_name}/definition/bookmarks/"

    # --- 2. Page source ---
    source_page_path = f"{pages_root}{source_page_name}/page.json"
    source_page = safe_json_load(files_dict.get(source_page_path), source_page_path)
    source_page_id = source_page["name"]

    # --- 3. Pages cibles ---
    pages_to_sync = []
    page_display_names = {}
    for path, content in files_dict.items():
        if path.startswith(pages_root) and path.endswith("page.json"):
            p_data = safe_json_load(content, path)
            p_id = p_data["name"]
            if p_id != source_page_id and (target_pages is None or p_id in target_pages):
                pages_to_sync.append(p_id)
                page_display_names[p_id] = p_data.get("displayName", p_id)

    # --- 4. Bookmarks source valides ---
    source_bookmarks = {}
    
    # On normalise bookmark_name en liste pour faciliter la comparaison
    filter_names = [bookmark_name] if isinstance(bookmark_name, str) else bookmark_name

    for path, content in files_dict.items():
        if path.startswith(bookmarks_root) and path.endswith(".json"):
            bk = safe_json_load(content, path)
            if bk:
                # Vérifie si le bookmark appartient à la page source
                is_on_source_page = bk.get("explorationState", {}).get("activeSection") == source_page_id
                b_id = bk.get("name")

                if is_on_source_page:
                    if bookmark_name is None or b_id in filter_names:
                        source_bookmarks[b_id] = bk
                        

    # --- 5. SYNCHRONISATION (MAJ + SUPPRESSION) ---
    existing_bk_paths = [p for p in files_dict.keys() if p.startswith(bookmarks_root)]

    for p_id in pages_to_sync:
        display_name = page_display_names[p_id]
        expected_names = [f"{b_id}_{p_id}" for b_id in source_bookmarks.keys()]

        # A. Nettoyage des orphelins (Suppression)
        for path in existing_bk_paths:
            fname = os.path.basename(path).replace(".bookmark.json", "")
            # Si le fichier appartient à cette page mais n'est plus dans la source
            if fname.endswith(f"_{p_id}") and fname not in expected_names:
                print(f"🗑️ Orphelin supprimé : {fname}")
                del files_dict[path]
                # Suppression physique si le fichier existe
                full_p = os.path.join(pbir_folder_path, path)
                if os.path.exists(full_p): os.remove(full_p)

        # B. Création / Modification
        for b_id, b_data in source_bookmarks.items():
            new_name = f"{b_id}_{p_id}"
            new_path = f"{bookmarks_root}{new_name}.bookmark.json"
            
            new_bk = copy.deepcopy(b_data)
            new_bk["name"] = new_name
            new_bk["displayName"] = f"{display_name}_{b_data.get('displayName', b_id)}"
            new_bk["explorationState"]["activeSection"] = p_id

            sections = new_bk["explorationState"].get("sections", {})
            if source_page_id in sections:
                sections[p_id] = sections.pop(source_page_id)

            files_dict[new_path] = json.dumps(new_bk, indent=2).encode("utf-8")

    # --- 6. Réaffectation Visuels ---
    vis_mapping = {}
    source_vis_prefix = f"{pages_root}{source_page_name}/visuals/"
    for path, content in files_dict.items():
        if path.startswith(source_vis_prefix) and path.endswith("visual.json"):
            v_id = path.split("/")[-2]
            vis = safe_json_load(content, path)
            for link in vis.get("visual", {}).get("visualContainerObjects", {}).get("visualLink", []):
                val = link.get("properties", {}).get("bookmark", {}).get("expr", {}).get("Literal", {}).get("Value", "").strip("'")
                if val in source_bookmarks:
                    vis_mapping[v_id] = val

    for p_id in pages_to_sync:
        for v_id, b_id_src in vis_mapping.items():
            target_v_path = f"{pages_root}{p_id}/visuals/{v_id}/visual.json"
            if target_v_path in files_dict:
                v_json = safe_json_load(files_dict[target_v_path], target_v_path)
                for link in v_json.get("visual", {}).get("visualContainerObjects", {}).get("visualLink", []):
                    link["properties"]["bookmark"]["expr"]["Literal"]["Value"] = f"'{b_id_src}_{p_id}'"
                files_dict[target_v_path] = json.dumps(v_json, indent=2).encode("utf-8")

    # --- 7. Sauvegarde ---
    for rel_path, content in files_dict.items():
        full_path = os.path.join(pbir_folder_path, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(content)

    print("🎉 Synchronisation des bookmarks terminée.")