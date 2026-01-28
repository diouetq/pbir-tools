"""
Exemple d'utilisation : Duplication de bookmarks entre pages
"""

from pbir_tools import pbir_duplicate_bookmark

# Configuration
PBIR_PATH = r"C:\Users\votre_nom\Documents\PowerBI\Report1"
REPORT_NAME = "Report1.Report"
SOURCE_PAGE = "main"
TARGET_PAGES = ["page2", "page3"]  # None pour toutes les pages
BOOKMARK_NAMES = None  # None pour tous les bookmarks, ou ["bookmark1", "bookmark2"]

if __name__ == "__main__":
    print("=" * 60)
    print("Duplication de bookmarks")
    print("=" * 60)
    print(f"Source : Page '{SOURCE_PAGE}'")
    print(f"Cibles : {TARGET_PAGES if TARGET_PAGES else 'Toutes les pages'}")
    print(f"Bookmarks : {BOOKMARK_NAMES if BOOKMARK_NAMES else 'Tous'}")
    print("=" * 60)
    print()
    
    # Dupliquer les bookmarks
    pbir_duplicate_bookmark(
        pbir_folder_path=PBIR_PATH,
        report_root_name=REPORT_NAME,
        source_page_name=SOURCE_PAGE,
        target_pages=TARGET_PAGES,
        bookmark_name=BOOKMARK_NAMES
    )
    
    print("\n✅ Synchronisation terminée avec succès !")
    print("⚠️  Note : Les bookmarks orphelins ont été automatiquement supprimés.")
    
    # Exemples d'autres utilisations :
    
    # Exemple 1 : Synchroniser tous les bookmarks vers toutes les pages
    # pbir_duplicate_bookmark(
    #     pbir_folder_path=PBIR_PATH,
    #     report_root_name=REPORT_NAME,
    #     source_page_name=SOURCE_PAGE,
    #     target_pages=None,
    #     bookmark_name=None
    # )
    
    # Exemple 2 : Dupliquer un bookmark spécifique
    # pbir_duplicate_bookmark(
    #     pbir_folder_path=PBIR_PATH,
    #     report_root_name=REPORT_NAME,
    #     source_page_name=SOURCE_PAGE,
    #     target_pages=["page2"],
    #     bookmark_name="b77245c801845ab0a4d5"
    # )
    
    # Exemple 3 : Dupliquer plusieurs bookmarks spécifiques
    # pbir_duplicate_bookmark(
    #     pbir_folder_path=PBIR_PATH,
    #     report_root_name=REPORT_NAME,
    #     source_page_name=SOURCE_PAGE,
    #     target_pages=None,
    #     bookmark_name=["b77245c801845ab0a4d5", "fb9c6b8b97750472c1a0"]
    # )
