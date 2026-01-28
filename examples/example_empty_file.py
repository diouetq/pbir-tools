"""
Exemple d'utilisation : Création d'un fichier PBIR vide
"""

from pbir_tools import pbir_empty_file

# Configuration
OUTPUT_FOLDER = r"C:\Users\votre_nom\Documents\PowerBI"
NEW_REPORT_NAME = "MonNouveauRapport"

if __name__ == "__main__":
    print("=" * 60)
    print("Création d'un nouveau rapport PBIR")
    print("=" * 60)
    
    # Créer le rapport
    pbir_empty_file(
        output_folder=OUTPUT_FOLDER,
        new_report_name=NEW_REPORT_NAME
    )
    
    print("\n✅ Rapport créé avec succès !")
    print(f"📁 Emplacement : {OUTPUT_FOLDER}")
    print(f"📄 Nom : {NEW_REPORT_NAME}")
    print("\nVous pouvez maintenant ouvrir ce fichier dans Power BI Desktop.")
