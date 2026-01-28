# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Prévu
- Interface en ligne de commande (CLI)
- Support pour les thèmes personnalisés
- Export de métadonnées en CSV
- Validation automatique des fichiers PBIR

---

## [1.0.0] - 2026-01-28

### 🎉 Version initiale

#### Ajouté
- ✨ **pbir_empty_file** : Création de fichiers PBIR vides avec structure complète
- ✨ **pbir_duplicate_visuals** : Duplication de visuels entre pages avec préservation de la mise en page
  - Support des groupes de visuels
  - Préservation de l'ordre des éléments
  - Gestion intelligente des z-index
- ✨ **pbir_duplicate_bookmark** : Duplication et synchronisation de bookmarks
  - Suppression automatique des bookmarks orphelins
  - Mise à jour des liens dans les visuels
  - Support des filtres de bookmarks spécifiques
- 📚 Documentation complète
  - README détaillé
  - Guide d'utilisation
  - Exemples d'utilisation pour chaque fonction
- 🧪 Tests unitaires de base
- 📦 Configuration de packaging (setup.py, pyproject.toml)
- 📝 Guide de contribution

#### Documentation
- Guide d'installation
- Exemples pratiques
- Documentation des API
- Bonnes pratiques

---

## Format

### Types de changements
- `Ajouté` pour les nouvelles fonctionnalités
- `Modifié` pour les changements dans les fonctionnalités existantes
- `Déprécié` pour les fonctionnalités qui seront bientôt supprimées
- `Supprimé` pour les fonctionnalités supprimées
- `Corrigé` pour les corrections de bugs
- `Sécurité` pour les vulnérabilités corrigées

[Non publié]: https://github.com/votre-username/pbir-tools/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/votre-username/pbir-tools/releases/tag/v1.0.0
