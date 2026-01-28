"""
PBIR Tools - Bibliothèque d'automatisation pour Power BI (Format PBIR)

Ce package fournit des outils pour manipuler et automatiser des rapports Power BI
au format PBIR (Power BI Project format).

Fonctionnalités principales:
- Création de fichiers PBIR vides
- Duplication de visuels entre pages
- Gestion des bookmarks

Example:
    >>> from pbir_tools import pbir_empty_file, pbir_duplicate_visuals
    >>> pbir_empty_file("/path/to/output", "MonRapport")
    >>> pbir_duplicate_visuals("/path/to/pbir", "Report", "main", ["page2"])
"""

from .empty_file import pbir_empty_file
from .visuals import pbir_duplicate_visuals
from .bookmarks import pbir_duplicate_bookmark

__version__ = "1.0.0"
__author__ = "DIOUET"

__all__ = [
    "pbir_empty_file",
    "pbir_duplicate_visuals",
    "pbir_duplicate_bookmark"
]
