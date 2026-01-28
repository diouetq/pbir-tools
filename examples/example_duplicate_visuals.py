"""
Exemple d'utilisation : Duplication de visuels entre pages
"""

from pbir_tools import pbir_duplicate_visuals

# Configuration
PBIR_PATH = r"C:\Users\votre_nom\Documents\PowerBI\Report1"
REPORT_NAME = "Report1.Report"
SOURCE_PAGE = "main"
TARGET_PAGES = ["page2", "page3"]  # None pour toutes les pages
VISUAL_NAMES = None  # None pour tous les visuels, ou ["Visuel 1", "Visuel 2"]

if __name__ == "__main__":
    print("=" * 60)
    print("Duplication de visuels")
    print("=" * 60)
    print(f"Source : Page '{SOURCE_PAGE}'")
    print(f"Cibles : {TARGET_PAGES if TARGET_PAGES else 'Toutes les pages'}")
    print(f"Visuels : {VISUAL_NAMES if VISUAL_NAMES else 'Tous'}")
    print("=" * 60)
    print()
    
    # Dupliquer les visuels
    pbir_duplicate_visuals(
        pbir_folder_path=PBIR_PATH,
        report_root_name=REPORT_NAME,
        source_page_name=SOURCE_PAGE,
        target_pages=TARGET_PAGES,
        visual_name=VISUAL_NAMES
    )
    
    print("\n✅ Duplication terminée avec succès !")
    
    # Exemples d'autres utilisations :
    
    # Exemple 1 : Copier tous les visuels vers toutes les pages
    # pbir_duplicate_visuals(
    #     pbir_folder_path=PBIR_PATH,
    #     report_root_name=REPORT_NAME,
    #     source_page_name=SOURCE_PAGE,
    #     target_pages=None,
    #     visual_name=None
    # )
    
    # Exemple 2 : Copier un visuel spécifique
    # pbir_duplicate_visuals(
    #     pbir_folder_path=PBIR_PATH,
    #     report_root_name=REPORT_NAME,
    #     source_page_name=SOURCE_PAGE,
    #     target_pages=["page2"],
    #     visual_name="Mon Graphique"
    # )
    
    # Exemple 3 : Copier plusieurs visuels spécifiques
    # pbir_duplicate_visuals(
    #     pbir_folder_path=PBIR_PATH,
    #     report_root_name=REPORT_NAME,
    #     source_page_name=SOURCE_PAGE,
    #     target_pages=None,
    #     visual_name=["Graphique 1", "Tableau 2", "KPI 3"]
    # )
