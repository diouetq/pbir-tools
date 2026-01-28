# PBIR Tools 🚀

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Bibliothèque Python pour l'automatisation et la manipulation de rapports Power BI au format PBIR (Power BI Project format).

## 📋 Fonctionnalités

- **Création de fichiers PBIR vides** : Génère rapidement des structures PBIR de base
- **Duplication de visuels** : Copie des visuels d'une page source vers plusieurs pages cibles en préservant la mise en page
- **Gestion des bookmarks** : Synchronise et duplique les bookmarks entre pages avec gestion automatique des orphelins

## 🔧 Installation

### Installation depuis GitHub

```bash
# Cloner le repository
git clone https://github.com/votre-username/pbir-tools.git
cd pbir-tools

# Installer le package
pip install -e .
```

### Installation en mode développement

```bash
# Cloner et installer avec les dépendances de développement
git clone https://github.com/votre-username/pbir-tools.git
cd pbir-tools
pip install -e ".[dev]"
```

## 📚 Utilisation

### 1. Créer un fichier PBIR vide

```python
from pbir_tools import pbir_empty_file

# Créer un nouveau rapport PBIR
pbir_empty_file(
    output_folder="C:/path/to/output",
    new_report_name="MonNouveauRapport"
)
```

### 2. Dupliquer des visuels entre pages

```python
from pbir_tools import pbir_duplicate_visuals

# Copier tous les visuels de la page "main" vers d'autres pages
pbir_duplicate_visuals(
    pbir_folder_path="C:/path/to/pbir/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2", "page3"],  # None = toutes les pages
    visual_name=None  # None = tous les visuels
)

# Copier un visuel spécifique
pbir_duplicate_visuals(
    pbir_folder_path="C:/path/to/pbir/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2"],
    visual_name="Mon Graphique"
)

# Copier plusieurs visuels spécifiques
pbir_duplicate_visuals(
    pbir_folder_path="C:/path/to/pbir/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=None,
    visual_name=["Graphique 1", "Tableau 2"]
)
```

### 3. Gérer les bookmarks

```python
from pbir_tools import pbir_duplicate_bookmark

# Dupliquer tous les bookmarks de la page source
pbir_duplicate_bookmark(
    pbir_folder_path="C:/path/to/pbir/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2", "page3"],
    bookmark_name=None  # None = tous les bookmarks
)

# Dupliquer un bookmark spécifique
pbir_duplicate_bookmark(
    pbir_folder_path="C:/path/to/pbir/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=["page2"],
    bookmark_name="mon_bookmark_id"
)

# Dupliquer plusieurs bookmarks
pbir_duplicate_bookmark(
    pbir_folder_path="C:/path/to/pbir/Report1",
    report_root_name="Report1.Report",
    source_page_name="main",
    target_pages=None,
    bookmark_name=["bookmark1", "bookmark2"]
)
```

## 📁 Structure du projet

```
pbir-tools/
├── pbir_tools/              # Package principal
│   ├── __init__.py
│   ├── empty_file.py        # Création de fichiers PBIR vides
│   ├── visuals.py           # Duplication de visuels
│   └── bookmarks.py         # Gestion des bookmarks
├── examples/                 # Scripts d'exemple
│   ├── example_empty_file.py
│   ├── example_duplicate_visuals.py
│   └── example_duplicate_bookmarks.py
├── tests/                    # Tests unitaires
│   ├── test_empty_file.py
│   ├── test_visuals.py
│   └── test_bookmarks.py
├── docs/                     # Documentation
│   └── usage.md
├── README.md
├── setup.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

## 🧪 Tests

```bash
# Exécuter tous les tests
pytest

# Exécuter les tests avec couverture
pytest --cov=pbir_tools tests/
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Changelog

### Version 1.0.0 (2026-01-28)
- 🎉 Version initiale
- ✨ Création de fichiers PBIR vides
- ✨ Duplication de visuels avec préservation de la mise en page
- ✨ Gestion synchronisée des bookmarks

## 📄 License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

**DIOUET**

## 🙏 Remerciements

- Microsoft Power BI pour le format PBIR
- La communauté Python

## 📞 Support

Pour toute question ou problème :
- Ouvrir une [issue](https://github.com/votre-username/pbir-tools/issues)
- Consulter la [documentation](docs/usage.md)

---

⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile !
