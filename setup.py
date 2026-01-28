"""Setup configuration for PBIR Tools."""

from setuptools import setup, find_packages
from pathlib import Path

# Lire le README pour la description longue
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pbir-tools",
    version="1.0.0",
    author="DIOUET",
    author_email="diouet.pro@gmail.com",  # À personnaliser
    description="Bibliothèque d'automatisation pour Power BI (Format PBIR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diouetq/pbir-tools",  # À personnaliser
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Pas de dépendances externes pour le moment
        # Uniquement la bibliothèque standard Python
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
    },
    entry_points={
        "console_scripts": [
            # Si vous souhaitez ajouter des commandes CLI plus tard
            # "pbir-tools=pbir_tools.cli:main",
        ],
    },
    keywords="powerbi pbir automation reporting",
    project_urls={
        "Bug Reports": "https://github.com/diouetq/pbir-tools/issues",
        "Source": "https://github.com/diouetq/pbir-tools",
        "Documentation": "https://github.com/diouetq/pbir-tools/blob/main/docs/usage.md",
    },
)
