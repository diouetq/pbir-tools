# 🚀 Guide de Démarrage Rapide - PBIR Tools

## Étapes pour publier sur GitHub

### 1. Initialiser le dépôt Git

```bash
cd pbir-tools
git init
git add .
git commit -m "🎉 Version initiale 1.0.0"
```

### 2. Créer un dépôt sur GitHub

1. Allez sur https://github.com
2. Cliquez sur "New repository"
3. Nom : `pbir-tools`
4. Description : `Bibliothèque d'automatisation pour Power BI (Format PBIR)`
5. Cochez "Public" (ou Private selon votre choix)
6. **NE PAS** cocher "Initialize with README" (vous en avez déjà un)
7. Cliquez sur "Create repository"

### 3. Lier et pousser vers GitHub

```bash
git remote add origin https://github.com/diouetq/pbir-tools.git
git branch -M main
git push -u origin main
```

### 4. Personnaliser les fichiers

Avant de pousser, modifiez ces éléments :

#### Dans `setup.py` :
- `author_email="votre.email@example.com"` → votre email
- `url="https://github.com/votre-username/pbir-tools"` → votre URL

#### Dans `pyproject.toml` :
- `email = "votre.email@example.com"` → votre email
- Toutes les URLs avec `votre-username`

#### Dans `README.md` :
- Remplacez `votre-username` par votre nom d'utilisateur GitHub

---

## Installation pour les utilisateurs

Une fois publié sur GitHub, les utilisateurs pourront installer avec :

```bash
pip install git+https://github.com/diouetq/pbir-tools.git
```

---

## Structure finale du projet

```
pbir-tools/
├── pbir_tools/                  # ✅ Package principal
│   ├── __init__.py              # ✅ Point d'entrée
│   ├── empty_file.py            # ✅ Création de fichiers vides
│   ├── visuals.py               # ✅ Duplication de visuels
│   └── bookmarks.py             # ✅ Gestion des bookmarks
├── examples/                     # ✅ Exemples d'utilisation
│   ├── example_empty_file.py
│   ├── example_duplicate_visuals.py
│   └── example_duplicate_bookmarks.py
├── tests/                        # ✅ Tests unitaires
│   ├── __init__.py
│   └── test_empty_file.py
├── docs/                         # ✅ Documentation
│   └── usage.md
├── README.md                     # ✅ Documentation principale
├── setup.py                      # ✅ Configuration pip (legacy)
├── pyproject.toml                # ✅ Configuration moderne
├── requirements.txt              # ✅ Dépendances
├── requirements-dev.txt          # ✅ Dépendances dev
├── .gitignore                    # ✅ Fichiers à ignorer
├── LICENSE                       # ✅ Licence MIT
├── CHANGELOG.md                  # ✅ Historique des versions
├── CONTRIBUTING.md               # ✅ Guide de contribution
└── MANIFEST.in                   # ✅ Fichiers à inclure

```

---

## Prochaines étapes

### Publier une release

1. Créez un tag de version :
```bash
git tag -a v1.0.0 -m "Version 1.0.0 - Release initiale"
git push origin v1.0.0
```

2. Sur GitHub, allez dans "Releases" → "Create a new release"
3. Sélectionnez le tag `v1.0.0`
4. Ajoutez les notes de version (copiez depuis CHANGELOG.md)
5. Publiez la release

### Publier sur PyPI (optionnel)

Pour rendre le package installable avec `pip install pbir-tools` :

```bash
# Installer les outils
pip install build twine

# Construire le package
python -m build

# Uploader sur PyPI (nécessite un compte)
twine upload dist/*
```

### Ajouter des badges au README

Ajoutez ces badges en haut du README :

```markdown
[![GitHub release](https://img.shields.io/github/v/release/diouetq/pbir-tools.svg)](https://github.com/diouetq/pbir-tools/releases)
[![GitHub issues](https://img.shields.io/github/issues/diouetq/pbir-tools.svg)](https://github.com/diouetq/pbir-tools/issues)
[![GitHub stars](https://img.shields.io/github/stars/diouetq/pbir-tools.svg)](https://github.com/diouetq/pbir-tools/stargazers)
```

---

## Utilisation par d'autres développeurs

### Installation

```bash
pip install git+https://github.com/diouetq/pbir-tools.git
```

### Exemple d'utilisation

```python
from pbir_tools import pbir_empty_file, pbir_duplicate_visuals

# Créer un rapport vide
pbir_empty_file("C:/output", "MonRapport")

# Dupliquer des visuels
pbir_duplicate_visuals(
    pbir_folder_path="C:/PowerBI/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2", "page3"]
)
```

---

## Bonnes pratiques maintenant que le projet est structuré

### 1. Branches

Utilisez des branches pour les nouvelles fonctionnalités :
```bash
git checkout -b feature/nouvelle-fonction
# Travaillez sur la fonctionnalité
git commit -m "✨ Ajout de nouvelle-fonction"
git push origin feature/nouvelle-fonction
# Créez une Pull Request sur GitHub
```

### 2. Issues

Créez des issues pour :
- Bugs
- Nouvelles fonctionnalités
- Améliorations
- Questions

### 3. Documentation

Maintenez à jour :
- README.md pour les changements majeurs
- CHANGELOG.md pour chaque version
- docs/usage.md pour les détails d'utilisation

### 4. Tests

Ajoutez des tests pour chaque nouvelle fonctionnalité :
```python
# tests/test_nouvelle_fonction.py
def test_nouvelle_fonction():
    # Votre test ici
    pass
```

---

## ✅ Checklist finale avant publication

- [ ] Remplacer `votre-username` par votre nom GitHub partout
- [ ] Remplacer `votre.email@example.com` par votre email
- [ ] Tester l'installation : `pip install -e .`
- [ ] Tester les exemples dans `examples/`
- [ ] Vérifier que `.gitignore` fonctionne
- [ ] Lire le README pour vérifier qu'il est clair
- [ ] Vérifier que la licence est appropriée

---

## 🎉 Félicitations !

Votre projet est maintenant structuré professionnellement et prêt à être partagé ! 

Pour toute question, consultez :
- Le README.md
- docs/usage.md
- Les exemples dans examples/
