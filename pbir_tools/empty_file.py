# -*- coding: utf-8 -*-
"""
Module pour créer des fichiers PBIR vides.
"""

import os


def is_text_file(content: bytes) -> bool:
    """Retourne True si le fichier est probablement du texte (UTF-8)."""
    try:
        content.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def pbir_empty_file(output_folder: str, new_report_name: str):
    """
    Recrée un report PBIR à partir du dictionnaire interne files_to_create.
    Remplace dynamiquement les occurrences de 'Base' ou 'Init_PBIR' par le nouveau nom.
    
    Args:
        output_folder (str): Chemin du dossier de sortie
        new_report_name (str): Nom du nouveau rapport à créer
        
    Example:
        >>> pbir_empty_file("/path/to/output", "MonNouveauRapport")
    """
    
    # --- DICTIONNAIRE INTÉGRÉ ---
    files_to_create = {
        ".gitignore": b'**/.pbi/localSettings.json\r\n**/.pbi/cache.abf',
        "Base.pbip": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json",\r\n  "version": "1.0",\r\n  "artifacts": [\r\n    {\r\n      "report": {\r\n        "path": "Base.Report"\r\n      }\r\n    }\r\n  ],\r\n  "settings": {\r\n    "enableAutoRecovery": true\r\n  }\r\n}',
        "Base.Report/.platform": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",\r\n  "metadata": {\r\n    "type": "Report",\r\n    "displayName": "Base"\r\n  },\r\n  "config": {\r\n    "version": "2.0",\r\n    "logicalId": "c8de1e35-7f0f-40e8-915b-4de5bd19afac"\r\n  }\r\n}',
        "Base.Report/definition.pbir": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",\r\n  "version": "4.0",\r\n  "datasetReference": {\r\n    "byPath": {\r\n      "path": "../Base.SemanticModel"\r\n    }\r\n  }\r\n}',
        "Base.Report/.pbi/localSettings.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/localSettings/1.0.0/schema.json",\r\n  "securityBindingsSignature": "AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAEvXDnSdjCU2DmptG1GFlIwAAAAACAAAAAAAQZgAAAAEAACAAAACT0kaSNXVNg5CeksF5/+QhzadLiDJ3Q4FHNOte67JthgAAAAAOgAAAAAIAACAAAADKwAxn4DhCTIvbRJOZj/LMz1/RoLbnNnlUAzJPVaYnorAAAADtc5QZFwSEvwpf8ChvHw1IrW6qboUBiTTogc3OiCEobimjgNiRxwCQQJWhELXJtgYaIwkHnhk9XRm6RaowmAs86mkPogIKbxT1F/LHPscXwtCqMLXmN0tB51UqRAI2YZxYoO0dHfQsYm0XcSMhUw6Jc7xtSa+7SKjTowtMseqdLMDNQgTEf3+mxpw6NJdqIJ3rNZWHQjquwfpBMnUaOea9/avPP76Gl/YwE4I+oGT+PUAAAAB8spBOvB23JXzDds23KWIZgZG0bOYLT8tTGedovAr/gFYCan2fb/eF60SQcHR+s5IyWBvtmFY1DysaZe86Ndms"\r\n}',
        "Base.Report/definition/report.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.0.0/schema.json",\r\n  "themeCollection": {\r\n    "baseTheme": {\r\n      "name": "CY25SU11",\r\n      "reportVersionAtImport": {\r\n        "visual": "2.4.0",\r\n        "report": "3.0.0",\r\n        "page": "2.3.0"\r\n      },\r\n      "type": "SharedResources"\r\n    }\r\n  },\r\n  "objects": {\r\n    "section": [\r\n      {\r\n        "properties": {\r\n          "verticalAlignment": {\r\n            "expr": {\r\n              "Literal": {\r\n                "Value": "\'Middle\'"\r\n              }\r\n            }\r\n          }\r\n        }\r\n      }\r\n    ]\r\n  },\r\n  "resourcePackages": [\r\n    {\r\n      "name": "SharedResources",\r\n      "type": "SharedResources",\r\n      "items": [\r\n        {\r\n          "name": "CY25SU11",\r\n          "path": "BaseThemes/CY25SU11.json",\r\n          "type": "BaseTheme"\r\n        }\r\n      ]\r\n    }\r\n  ],\r\n  "settings": {\r\n    "useStylableVisualContainerHeader": true,\r\n    "exportDataMode": "AllowSummarized",\r\n    "defaultDrillFilterOtherVisuals": true,\r\n    "allowChangeFilterTypes": true,\r\n    "useEnhancedTooltips": true,\r\n    "useDefaultAggregateDisplayName": true\r\n  }\r\n}',
        "Base.Report/definition/version.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",\r\n  "version": "2.0.0"\r\n}',
        "Base.Report/definition/pages/pages.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",\r\n  "pageOrder": [\r\n    "42ce56b32d11a4101cb7"\r\n  ],\r\n  "activePageName": "42ce56b32d11a4101cb7"\r\n}',
        "Base.Report/definition/pages/42ce56b32d11a4101cb7/page.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.3.0/schema.json",\r\n  "name": "42ce56b32d11a4101cb7",\r\n  "displayName": "Page 1"\r\n}',
        "Base.SemanticModel/.platform": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",\r\n  "metadata": {\r\n    "type": "SemanticModel",\r\n    "displayName": "Base"\r\n  },\r\n  "config": {\r\n    "version": "2.0",\r\n    "logicalId": "73e31feb-9e37-4279-8cd6-f4c2a2a8f6a5"\r\n  }\r\n}',
        "Base.SemanticModel/.pbi/editorSettings.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/editorSettings/1.0.0/schema.json",\r\n  "autodetectRelationships": true,\r\n  "parallelQueryLoading": true,\r\n  "typeDetectionEnabled": true,\r\n  "relationshipImportEnabled": true,\r\n  "shouldNotifyUserOfNameConflictResolution": true\r\n}',
        "Base.SemanticModel/.pbi/localSettings.json": b'{\r\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/localSettings/1.2.0/schema.json",\r\n  "userConsent": {},\r\n  "securityBindingsSignature": "AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAEvXDnSdjCU2DmptG1GFlIwAAAAACAAAAAAAQZgAAAAEAACAAAAA5t6XU/27YKdc1sgBsLK3b6YsAt64vcZVoBvr655WNmQAAAAAOgAAAAAIAACAAAADp3pPDXhGRyFY2vHVE/U5XpLAlyPrIYaoB1dzwnWMJe1AAAAChyiffxYRvvApSz8MHV1njUB3g1TdOFfGFjMSoH1k304J1Olots/m63rjPLwzjjyTpBgTmb8Dc/HzWirpYRbYQR5sNrTjy0fymJRnqmM29ZEAAAADjjXjABb0gBZ1qfqOgh5AMIsxS/4bs0Vhnb5Z8qUrL5QqgLW4hrYOesQwugzSpSwao7dI8YrtIL13uY5H3h7cZ"\r\n}',
        "Base.SemanticModel/definition/database.tmdl": b'database\r\n\tcompatibilityLevel: 1550\r\n\r\n',
        "Base.SemanticModel/definition/model.tmdl": b'model Model\r\n\tculture: fr-FR\r\n\tdefaultPowerBIDataSourceVersion: powerBI_V3\r\n\tsourceQueryCulture: fr-FR\r\n\tdataAccessOptions\r\n\t\tlegacyRedirects\r\n\t\treturnErrorValuesAsNull\r\n\r\nannotation __PBI_TimeIntelligenceEnabled = 1\r\n\r\nannotation PBI_ProTooling = ["DevMode"]\r\n\r\nref cultureInfo fr-FR\r\n\r\n',
        "Base.SemanticModel/definition/cultures/fr-FR.tmdl": b'cultureInfo fr-FR\r\n\r\n\tlinguisticMetadata =\r\n\t\t\t{\r\n\t\t\t  "Version": "1.0.0",\r\n\t\t\t  "Language": "en-US"\r\n\t\t\t}\r\n\t\tcontentType: json\r\n\r\n',
    }

    # Création des fichiers
    for relative_path, content in files_to_create.items():
        # 1. Remplacer 'Base' dans le NOM du fichier/dossier
        new_relative_path = relative_path.replace("Base", new_report_name)
        
        full_path = os.path.join(output_folder, new_relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # 2. Remplacer 'Base' dans le CONTENU si c'est du texte
        if is_text_file(content):
            text_content = content.decode("utf-8")
            text_content = text_content.replace("Base", new_report_name)
            content_to_write = text_content.encode("utf-8")
        else:
            # Si c'est un binaire, on écrit tel quel
            content_to_write = content

        with open(full_path, 'wb') as f:
            f.write(content_to_write)

    print(f"✔ Report PBIR '{new_report_name}' recréé avec succès dans : {output_folder}")
