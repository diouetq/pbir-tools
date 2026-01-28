# Guide de contribution

Merci de votre intérêt pour contribuer à PBIR Tools ! 🎉

## Comment contribuer

### 1. Fork et Clone

```bash
# Fork le projet sur GitHub puis clonez votre fork
git clone https://github.com/votre-username/pbir-tools.git
cd pbir-tools
```

### 2. Créer une branche

```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

### 3. Installer les dépendances de développement

```bash
pip install -e ".[dev]"
# ou
pip install -r requirements-dev.txt
```

### 4. Faire vos modifications

- Suivez les conventions de codage Python (PEP 8)
- Ajoutez des docstrings à vos fonctions
- Commentez le code complexe

### 5. Tester vos modifications

```bash
# Exécuter les tests
pytest

# Vérifier la couverture
pytest --cov=pbir_tools tests/

# Vérifier le style de code
black pbir_tools/
flake8 pbir_tools/
```

### 6. Commit et Push

```bash
git add .
git commit -m "✨ Ajout de la fonctionnalité X"
git push origin feature/ma-nouvelle-fonctionnalite
```

### 7. Créer une Pull Request

Allez sur GitHub et créez une Pull Request depuis votre branche vers `main`.

## Standards de code

### Style

- Utilisez **Black** pour le formatage : `black pbir_tools/`
- Suivez **PEP 8**
- Longueur de ligne : 88 caractères (Black)

### Documentation

```python
def ma_fonction(param1: str, param2: int) -> bool:
    """
    Description courte de la fonction.
    
    Description plus détaillée si nécessaire.
    
    Args:
        param1 (str): Description du paramètre 1
        param2 (int): Description du paramètre 2
        
    Returns:
        bool: Description de ce qui est retourné
        
    Example:
        >>> ma_fonction("test", 42)
        True
    """
    pass
```

### Tests

- Ajoutez des tests pour toute nouvelle fonctionnalité
- Maintenez la couverture de code > 80%
- Utilisez `pytest` pour les tests

```python
def test_ma_fonction():
    """Test de ma_fonction"""
    result = ma_fonction("test", 42)
    assert result is True
```

## Conventions de commit

Utilisez des préfixes pour vos messages de commit :

- ✨ `:sparkles:` Nouvelle fonctionnalité
- 🐛 `:bug:` Correction de bug
- 📝 `:memo:` Documentation
- ♻️ `:recycle:` Refactoring
- ✅ `:white_check_mark:` Tests
- 🎨 `:art:` Amélioration du style/format
- ⚡ `:zap:` Performance
- 🔧 `:wrench:` Configuration

Exemple :
```bash
git commit -m "✨ Ajout de la fonction de validation des bookmarks"
```

## Types de contributions

### Bugs

Si vous trouvez un bug :
1. Vérifiez qu'il n'existe pas déjà dans les [issues](https://github.com/votre-username/pbir-tools/issues)
2. Créez une nouvelle issue avec :
   - Description claire du problème
   - Étapes pour reproduire
   - Comportement attendu vs actuel
   - Version de Python et du package

### Nouvelles fonctionnalités

1. Ouvrez d'abord une issue pour discuter de la fonctionnalité
2. Attendez l'approbation avant de commencer le développement
3. Créez une Pull Request avec :
   - Code testé
   - Documentation mise à jour
   - Exemples d'utilisation

### Documentation

- Corrections de typos
- Améliorations de clarté
- Ajout d'exemples
- Traductions

Toutes les contributions à la documentation sont les bienvenues !

## Processus de revue

1. Un mainteneur examinera votre PR dans les 7 jours
2. Des modifications peuvent être demandées
3. Une fois approuvée, la PR sera mergée
4. Votre nom sera ajouté aux contributeurs ! 🎉

## Questions ?

N'hésitez pas à :
- Ouvrir une [issue](https://github.com/votre-username/pbir-tools/issues)
- Demander de l'aide dans les discussions
- Contacter les mainteneurs

## Code de conduite

Soyez respectueux, inclusif et professionnel dans toutes les interactions.

---

Merci de contribuer à PBIR Tools ! 🙏
