# Guide d'utilisation - PBIR Tools

Ce guide détaille l'utilisation de chaque fonction du package PBIR Tools.

## Table des matières

1. [Installation](#installation)
2. [pbir_empty_file](#pbir_empty_file)
3. [pbir_duplicate_visuals](#pbir_duplicate_visuals)
4. [pbir_duplicate_bookmark](#pbir_duplicate_bookmark)
5. [Bonnes pratiques](#bonnes-pratiques)
6. [Résolution de problèmes](#résolution-de-problèmes)

---

## Installation

### Méthode 1 : Installation depuis GitHub

```bash
pip install git+https://github.com/votre-username/pbir-tools.git
```

### Méthode 2 : Installation locale

```bash
git clone https://github.com/votre-username/pbir-tools.git
cd pbir-tools
pip install -e .
```

---

## pbir_empty_file

Crée un nouveau fichier PBIR vide avec la structure de base nécessaire.

### Syntaxe

```python
pbir_empty_file(output_folder: str, new_report_name: str)
```

### Paramètres

- **output_folder** (str) : Chemin du dossier où créer le rapport
- **new_report_name** (str) : Nom du nouveau rapport (sans extension)

### Exemple

```python
from pbir_tools import pbir_empty_file

pbir_empty_file(
    output_folder="C:/Users/John/Documents/PowerBI",
    new_report_name="MonRapport2026"
)
```

### Résultat

Crée la structure suivante :
```
MonRapport2026/
├── MonRapport2026.pbip
├── MonRapport2026.Report/
│   ├── .platform
│   ├── definition.pbir
│   └── definition/
└── MonRapport2026.SemanticModel/
    ├── .platform
    └── definition/
```

---

## pbir_duplicate_visuals

Duplique des visuels d'une page source vers des pages cibles en préservant la mise en page, les groupes et l'ordre des éléments.

### Syntaxe

```python
pbir_duplicate_visuals(
    pbir_folder_path: str,
    report_root_name: str,
    source_page_name: str = "main",
    target_pages: list = None,
    visual_name = None
)
```

### Paramètres

- **pbir_folder_path** (str) : Chemin vers le dossier PBIR décompressé
- **report_root_name** (str) : Nom du rapport (ex: "Report1.Report")
- **source_page_name** (str) : Nom de la page source (défaut: "main")
- **target_pages** (list, optional) : Liste des pages cibles. Si None, copie vers toutes les pages
- **visual_name** (str, list, optional) : Nom(s) du/des visuel(s) à copier. Si None, copie tous les visuels

### Exemples

#### Exemple 1 : Copier tous les visuels vers toutes les pages

```python
from pbir_tools import pbir_duplicate_visuals

pbir_duplicate_visuals(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="template"
)
```

#### Exemple 2 : Copier vers des pages spécifiques

```python
pbir_duplicate_visuals(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2", "page3", "page4"]
)
```

#### Exemple 3 : Copier un visuel spécifique

```python
pbir_duplicate_visuals(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2"],
    visual_name="Mon Graphique Principal"
)
```

#### Exemple 4 : Copier plusieurs visuels spécifiques

```python
pbir_duplicate_visuals(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=None,
    visual_name=["KPI Ventes", "Graphique Mensuel", "Tableau Détails"]
)
```

### Comportement

- Les visuels sont placés **au-dessus** des visuels existants (z-index supérieur)
- L'ordre relatif des visuels copiés est préservé
- Les groupes sont créés ou mis à jour automatiquement
- Les propriétés de mise en page sont conservées

---

## pbir_duplicate_bookmark

Duplique et synchronise des bookmarks d'une page source vers des pages cibles avec gestion automatique des orphelins.

### Syntaxe

```python
pbir_duplicate_bookmark(
    pbir_folder_path: str,
    report_root_name: str,
    source_page_name: str = "main",
    target_pages: list = None,
    bookmark_name = None
)
```

### Paramètres

- **pbir_folder_path** (str) : Chemin vers le dossier PBIR
- **report_root_name** (str) : Nom du rapport
- **source_page_name** (str) : Page source (défaut: "main")
- **target_pages** (list, optional) : Pages cibles. Si None, toutes les pages
- **bookmark_name** (str, list, optional) : ID(s) du/des bookmark(s). Si None, tous les bookmarks

### Exemples

#### Exemple 1 : Synchroniser tous les bookmarks

```python
from pbir_tools import pbir_duplicate_bookmark

pbir_duplicate_bookmark(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main"
)
```

#### Exemple 2 : Synchroniser un bookmark spécifique

```python
pbir_duplicate_bookmark(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2", "page3"],
    bookmark_name="b77245c801845ab0a4d5"
)
```

#### Exemple 3 : Synchroniser plusieurs bookmarks

```python
pbir_duplicate_bookmark(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=None,
    bookmark_name=["bookmark_id_1", "bookmark_id_2"]
)
```

### Comportement

- Les bookmarks sont créés ou mis à jour sur les pages cibles
- Les bookmarks orphelins (qui n'existent plus dans la source) sont **automatiquement supprimés**
- Les liens dans les visuels sont mis à jour pour pointer vers les nouveaux bookmarks
- Le nom d'affichage du bookmark inclut le nom de la page cible

### ⚠️ Important

Les bookmarks orphelins sont supprimés automatiquement. Si un bookmark n'existe plus dans la page source, il sera supprimé de toutes les pages cibles lors de la synchronisation.

---

## Bonnes pratiques

### 1. Sauvegarde avant modification

Toujours créer une copie de votre fichier PBIR avant d'exécuter des scripts :

```python
import shutil

# Créer une sauvegarde
shutil.copytree(
    "C:/PowerBI/Report1",
    "C:/PowerBI/Report1_backup"
)
```

### 2. Vérifier les chemins

Assurez-vous que les chemins sont corrects :

```python
import os

pbir_path = "C:/PowerBI/Report1"
if not os.path.exists(pbir_path):
    raise FileNotFoundError(f"Le dossier {pbir_path} n'existe pas")
```

### 3. Tester sur une page d'abord

Testez d'abord sur une seule page cible :

```python
pbir_duplicate_visuals(
    pbir_folder_path=PBIR_PATH,
    report_root_name=REPORT_NAME,
    source_page_name="main",
    target_pages=["test_page"],  # Une seule page pour tester
    visual_name=None
)
```

### 4. Utiliser des noms de pages explicites

Évitez les IDs générés, utilisez des noms significatifs dans Power BI.

### 5. Versionner avec Git

Utilisez Git pour versionner vos fichiers PBIR :

```bash
cd C:/PowerBI/Report1
git init
git add .
git commit -m "Version initiale avant modifications"
```

---

## Résolution de problèmes

### Erreur : "Le dossier n'existe pas"

**Cause** : Le chemin du dossier PBIR est incorrect.

**Solution** :
```python
import os
print(os.path.abspath("votre_chemin"))  # Vérifier le chemin absolu
```

### Erreur : "Page source introuvable"

**Cause** : Le nom de la page source ne correspond pas.

**Solution** : Vérifier le nom exact de la page dans `pages/pages.json` :
```python
import json

with open("Report1.Report/definition/pages/pages.json") as f:
    pages = json.load(f)
    print(pages["pageOrder"])
```

### Les visuels ne s'affichent pas correctement

**Cause** : Conflit de z-index ou de groupes.

**Solution** : Réorganiser manuellement dans Power BI Desktop après l'import.

### Les bookmarks ne fonctionnent pas

**Cause** : Les IDs de bookmarks ont changé ou les visuels liés n'existent pas.

**Solution** :
1. Vérifier que les visuels sources existent sur les pages cibles
2. Recréer les liens manuellement dans Power BI si nécessaire

---

## Support

Pour toute question ou problème :
- Ouvrir une [issue sur GitHub](https://github.com/votre-username/pbir-tools/issues)
- Consulter les [exemples](../examples/)
- Lire le [README](../README.md)

---

**Dernière mise à jour** : 28 janvier 2026
