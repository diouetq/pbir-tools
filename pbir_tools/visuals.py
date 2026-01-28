# -*- coding: utf-8 -*-

"""
PBIR - Copier-coller de mise en page avec respect total de l'ordre

Reproduction exacte de la mise en page source sur les pages cibles :
- Ordre des groupes respecté
- Ordre des visuels dans les groupes respecté
- Visuels collés toujours au-dessus de l'existant
- Position z calculée intelligemment
"""

import os
import json

# ===== Extraire le nom lisible d'un visuel =====
def get_vis_name(vis):
    """
    Retourne le nom lisible du visuel pour le matching.
    Fallback sur le name du container si absent.
    """
    try:
        value = vis["visualContainerObjects"]["title"][0]["properties"]["text"]["expr"]["Literal"]["Value"]
        return value.strip("'").strip()
    except Exception:
        return vis.get("name", "").strip()

# ===== Merge visual =====
def merge_visual(source, target):
    """Fusionne un visuel source avec un visuel cible existant"""
    merged = source.copy()
    
    # Conserver les propriétés d'identité de la cible si elle existe
    for key in ("id", "name"):
        if key in target:
            merged[key] = target[key]
    
    return merged

# ===== Merge group =====
def merge_group(source, target, copied_visual_ids):
    """Fusionne un groupe source avec un groupe cible existant"""
    merged = source.copy()
    
    # Conserver les propriétés d'identité de la cible si elle existe
    for key in ("id", "name"):
        if key in target:
            merged[key] = target[key]
    
    # 🔹 Gestion de la liste des visuels : ordre source préservé + existants à la fin
    source_visuals = source.get("visuals", [])
    existing_visuals = target.get("visuals", []) if target else []
    
    print(f"\n    DEBUG merge_group:")
    print(f"      source_visuals: {source_visuals}")
    print(f"      existing_visuals: {existing_visuals}")
    print(f"      copied_visual_ids: {list(copied_visual_ids)}")
    
    # Les visuels copiés viennent en premier (ordre source)
    new_visuals = [v for v in source_visuals if v in copied_visual_ids]
    print(f"      new_visuals (copiés): {new_visuals}")
    
    # Puis les visuels déjà présents qui ne sont pas en train d'être écrasés
    copied_ids_set = set(copied_visual_ids)
    for vis_id in existing_visuals:
        if vis_id not in copied_ids_set:
            new_visuals.append(vis_id)
    
    print(f"      new_visuals (final): {new_visuals}")
    
    if new_visuals:
        merged["visuals"] = new_visuals
    
    return merged

# ===== Calcul du z : visuels collés au-dessus de l'existant =====
def compute_z_above_existing(vis_id, source_visuals_z_order, target_page_visuals, visual_id_mapping):
    """
    Calcule le z en plaçant les visuels collés au-dessus de tout ce qui existe.
    Respecte l'ordre relatif entre les visuels collés basé sur l'ordre source ORIGINAL.
    """
    # Trouver le z maximum de la page cible
    all_target = list(target_page_visuals.values())
    all_zs = [v.get("position", {}).get("z", 0) for v in all_target]
    max_z_target = max(all_zs) if all_zs else 0
    
    # Obtenir l'ordre des visuels dans la source (triés par z ORIGINAL)
    source_sorted = sorted(
        visual_id_mapping.items(),
        key=lambda x: source_visuals_z_order.get(x[0], 0)
    )
    
    # Trouver la position de ce visuel dans l'ordre source
    source_ids = [sid for sid, _ in source_sorted]
    idx = source_ids.index(vis_id)
    
    # Calculer le z : au-dessus de l'existant + offset selon position dans source
    # On garde un écart de 1 entre chaque visuel collé
    z = max_z_target + 1 + idx
    
    return z

# ===== FONCTION PRINCIPALE : DUPLICATION DE VISUELS =====

def pbir_duplicate_visuals(
    pbir_folder_path: str,
    report_root_name: str,
    source_page_name: str = "main",
    target_pages: list = None,
    visual_name=None
):
    """
    Duplique des visuels d'une page source vers des pages cibles en respectant la mise en page.
    
    Args:
        pbir_folder_path: Chemin vers le dossier PBIR décompressé
        report_root_name: Nom du rapport (ex: "Report")
        source_page_name: Nom de la page source (défaut: "main")
        target_pages: Liste des pages cibles (None = toutes sauf source)
        visual_name: Nom(s) des visuels à copier (str, list ou None = tous)
    
    Exemples:
        # Copier tous les visuels
        duplicate_visuals("path/to/pbir", "Report", "template")
        
        # Copier un visuel spécifique
        duplicate_visuals("path/to/pbir", "Report", "main", ["page1"], "Mon Graphique")
        
        # Copier plusieurs visuels
        duplicate_visuals("path/to/pbir", "Report", "main", None, ["Graphique 1", "Tableau 2"])
    """
    # Normaliser visual_name
    if visual_name is not None:
        if isinstance(visual_name, str):
            visual_name = [visual_name]
        elif not isinstance(visual_name, list):
            raise ValueError("visual_name doit être string, list ou None")
        visual_name = [v.strip().upper() for v in visual_name]

    # ===== CHARGEMENT DES FICHIERS =====
    print("📂 Chargement des fichiers PBIR...")
    files_dict = {}
    for root, dirs, files in os.walk(pbir_folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, pbir_folder_path).replace("\\", "/")
            with open(full_path, "rb") as f:
                files_dict[rel_path] = f.read()

    pages_prefix = f"{report_root_name}/definition/pages/"
    source_visuals_prefix = f"{pages_prefix}{source_page_name}/visuals/"

    # ===== CHARGEMENT DE LA PAGE SOURCE =====
    print(f"\n📄 Analyse de la page source : {source_page_name}")
    
    # Charger page.json source
    source_page_json_path = f"{pages_prefix}{source_page_name}/page.json"
    source_page_data = {}
    if source_page_json_path in files_dict:
        source_page_data = json.loads(files_dict[source_page_json_path].decode("utf-8"))
    
    # Charger tous les visuels de la source
    all_source_visuals = {}
    for path, content in files_dict.items():
        if path.startswith(source_visuals_prefix) and path.endswith("visual.json"):
            vis_id = path.split("/")[-2]
            vis_json = json.loads(content.decode("utf-8"))
            all_source_visuals[vis_id] = vis_json
    
    # 🔹 IMPORTANT : Créer une copie immuable de l'ordre source pour ne pas qu'il soit modifié
    source_visuals_z_order = {
        vis_id: vis.get("position", {}).get("z", 0) 
        for vis_id, vis in all_source_visuals.items()
    }

    # Charger tous les groupes de la source
    source_groups = {}
    for path, content in files_dict.items():
        if path.startswith(source_visuals_prefix) and path.endswith("group.json"):
            group_id = path.split("/")[-2]
            group_json = json.loads(content.decode("utf-8"))
            source_groups[group_id] = group_json

    # ===== FILTRAGE DES VISUELS À COPIER =====
    print("\n🔍 Sélection des visuels à copier...")
    visuals_to_copy = {}
    groups_to_copy = set()
    
    for vis_id, vis_json in all_source_visuals.items():
        vis_name_lisible = get_vis_name(vis_json)
        
        # Filtrage par nom si spécifié
        if visual_name and vis_name_lisible.upper() not in visual_name:
            continue
        
        visuals_to_copy[vis_id] = vis_json
        print(f"  ✓ {vis_name_lisible} (id: {vis_id})")
        
        # Identifier les groupes nécessaires
        if "parentGroupName" in vis_json:
            groups_to_copy.add(vis_json["parentGroupName"])

    if not visuals_to_copy:
        raise ValueError("❌ Aucun visuel trouvé à copier")

    print(f"\n📊 {len(visuals_to_copy)} visuel(s) à copier")
    if groups_to_copy:
        print(f"📁 {len(groups_to_copy)} groupe(s) nécessaire(s) : {list(groups_to_copy)}")

    # ===== DÉTERMINATION DES PAGES CIBLES =====
    all_pages = []
    for path in files_dict:
        if path.startswith(pages_prefix) and path.endswith("page.json"):
            page = path[len(pages_prefix):].split("/")[0]
            if page != source_page_name:
                all_pages.append(page)

    if target_pages is None:
        target_pages = all_pages
    else:
        for p in target_pages:
            if p not in all_pages:
                raise ValueError(f"❌ Page cible inconnue : {p}")

    print(f"\n🎯 Pages cibles : {target_pages}")

    # ===== DUPLICATION SUR CHAQUE PAGE CIBLE =====
    for page in target_pages:
        print(f"\n{'='*60}")
        print(f"🔄 Traitement de la page : {page}")
        print(f"{'='*60}")
        
        target_visuals_prefix = f"{pages_prefix}{page}/visuals/"
        page_json_path = f"{pages_prefix}{page}/page.json"

        # Charger les visuels et groupes existants de la cible
        target_page_visuals = {}
        target_groups = {}
        
        for path, content in files_dict.items():
            if path.startswith(target_visuals_prefix):
                if path.endswith("visual.json"):
                    vid = path.split("/")[-2]
                    target_page_visuals[vid] = json.loads(content.decode("utf-8"))
                elif path.endswith("group.json"):
                    gid = path.split("/")[-2]
                    target_groups[gid] = json.loads(content.decode("utf-8"))

        # ===== ÉTAPE 1 : COPIER LES GROUPES =====
        if groups_to_copy:
            print("\n📁 Copie des groupes...")
        copied_visual_ids = set(visuals_to_copy.keys())
        
        for group_id in groups_to_copy:
            if group_id in source_groups:
                source_group = source_groups[group_id]
                target_group = target_groups.get(group_id, {})
                
                merged_group = merge_group(source_group, target_group, copied_visual_ids)
                
                group_path = f"{target_visuals_prefix}{group_id}/group.json"
                files_dict[group_path] = json.dumps(merged_group, indent=2).encode("utf-8")
                target_groups[group_id] = merged_group
                
                status = "mis à jour" if target_group else "créé"
                print(f"  ✓ Groupe {status} : {group_id}")
                if "visuals" in merged_group:
                    print(f"    └─ Ordre : {merged_group['visuals']}")

        # ===== ÉTAPE 2 : METTRE À JOUR page.json (ordre des groupes) =====
        if page_json_path in files_dict:
            print("\n📋 Mise à jour de l'ordre des groupes dans page.json...")
            
            target_page_data = json.loads(files_dict[page_json_path].decode("utf-8"))
            
            # Liste des groupes existants et source
            existing_groups = target_page_data.get("visualContainers", [])
            source_groups_list = source_page_data.get("visualContainers", [])
            
            print(f"  ℹ Ordre source : {source_groups_list}")
            print(f"  ℹ Ordre cible avant : {existing_groups}")
            
            # Créer un set pour check rapide
            groups_to_copy_set = set(groups_to_copy)
            existing_groups_set = set(existing_groups)
            
            # NOUVELLE LOGIQUE : Construire l'ordre final en respectant l'ordre source
            new_groups_list = []
            
            # Parcourir l'ordre de la source et ajouter les groupes dans cet ordre
            for group_id in source_groups_list:
                if group_id in groups_to_copy_set:
                    # Ce groupe est copié, l'ajouter dans l'ordre source
                    new_groups_list.append(group_id)
            
            # Ajouter les groupes existants qui ne sont PAS copiés (ils restent après)
            for group_id in existing_groups:
                if group_id not in groups_to_copy_set:
                    new_groups_list.append(group_id)
            
            print(f"  ℹ Ordre cible après : {new_groups_list}")
            
            if new_groups_list != existing_groups:
                target_page_data["visualContainers"] = new_groups_list
                files_dict[page_json_path] = json.dumps(target_page_data, indent=2).encode("utf-8")
                print(f"  ✓ Ordre des groupes mis à jour")
            else:
                print(f"  ℹ Ordre des groupes inchangé")

        # ===== ÉTAPE 3 : COPIER LES VISUELS =====
        print("\n🖼️  Copie des visuels...")
        
        # Créer un mapping pour calculer les z
        visual_id_mapping = {vid: vid for vid in visuals_to_copy.keys()}
        
        # 🔹 IMPORTANT : Trier les visuels par ordre de z source pour les traiter dans le bon ordre
        source_order = sorted(visuals_to_copy.items(), key=lambda x: source_visuals_z_order.get(x[0], 0))
        print(f"\n  📊 Ordre dans la source ORIGINAL (par z):")
        for vis_id, vis in source_order:
            z = source_visuals_z_order.get(vis_id, 0)
            parent = vis.get("parentGroupName", "aucun")
            print(f"    • {get_vis_name(vis)} : z={z}, groupe={parent}")
        
        # 🔹 ITÉRER SUR LES VISUELS DANS L'ORDRE DE Z SOURCE
        for vis_id, source_vis in source_order:
            target_path = f"{target_visuals_prefix}{vis_id}/visual.json"
            target_vis = target_page_visuals.get(vis_id, {})

            merged_vis = merge_visual(source_vis, target_vis)

            # Calculer le z : au-dessus de l'existant
            new_z = compute_z_above_existing(
                vis_id,
                source_visuals_z_order,  # 🔹 Utiliser l'ordre Z ORIGINAL
                target_page_visuals,
                visual_id_mapping
            )
            
            if "position" in merged_vis:
                merged_vis["position"]["z"] = new_z

            files_dict[target_path] = json.dumps(merged_vis, indent=2).encode("utf-8")
            target_page_visuals[vis_id] = merged_vis

            status = "Mis à jour" if target_vis else "Créé"
            vis_name = get_vis_name(merged_vis)
            parent = merged_vis.get("parentGroupName", "aucun")
            print(f"  ✓ {status} : {vis_name} (z={new_z}, groupe={parent})")

        # ===== ÉTAPE 4 : MISE À JOUR RAPPEL_PAGE_H SI PRÉSENT =====
        rappel_path = f"{target_visuals_prefix}Rappel_Page_H/visual.json"
        if rappel_path in files_dict:
            print(f"\n📝 Mise à jour de Rappel_Page_H...")
            
            rappel_vis = json.loads(files_dict[rappel_path].decode("utf-8"))
            
            # Obtenir le nom d'affichage de la page
            if page_json_path in files_dict:
                target_page_data = json.loads(files_dict[page_json_path].decode("utf-8"))
                display_name = target_page_data.get("displayName", page)
                
                # Mettre à jour le textRun[1] avec le nom de la page
                for g in rappel_vis.get("visual", {}).get("objects", {}).get("general", []):
                    for p in g.get("properties", {}).get("paragraphs", []):
                        runs = p.get("textRuns", [])
                        if len(runs) >= 2:
                            runs[1]["value"] = display_name
                            print(f"  ✓ Nom mis à jour : '{display_name}'")
                
                # Sauvegarder
                files_dict[rappel_path] = json.dumps(rappel_vis, indent=2).encode("utf-8")

    # ===== SAUVEGARDE =====
    print(f"\n{'='*60}")
    print("💾 Sauvegarde des modifications...")
    for rel_path, content in files_dict.items():
        full_path = os.path.join(pbir_folder_path, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as f:
            f.write(content)

    print("\n🎉 Duplication terminée avec succès !")
    print(f"   • {len(visuals_to_copy)} visuel(s) copié(s)")
    print(f"   • {len(target_pages)} page(s) mise(s) à jour")
