"""
Tests unitaires pour le module empty_file
"""

import os
import tempfile
import shutil
import pytest
from pbir_tools import pbir_empty_file


class TestPbirEmptyFile:
    """Tests pour la fonction pbir_empty_file"""
    
    def setup_method(self):
        """Créer un dossier temporaire pour chaque test"""
        self.test_dir = tempfile.mkdtemp()
    
    def teardown_method(self):
        """Nettoyer le dossier temporaire après chaque test"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_create_empty_file_basic(self):
        """Test de création basique d'un fichier PBIR vide"""
        report_name = "TestReport"
        
        pbir_empty_file(self.test_dir, report_name)
        
        # Vérifier que le fichier .pbip existe
        pbip_file = os.path.join(self.test_dir, f"{report_name}.pbip")
        assert os.path.exists(pbip_file)
        
        # Vérifier que le dossier Report existe
        report_folder = os.path.join(self.test_dir, f"{report_name}.Report")
        assert os.path.isdir(report_folder)
        
        # Vérifier que le dossier SemanticModel existe
        semantic_folder = os.path.join(self.test_dir, f"{report_name}.SemanticModel")
        assert os.path.isdir(semantic_folder)
    
    def test_create_empty_file_with_special_chars(self):
        """Test avec des caractères spéciaux dans le nom"""
        report_name = "Test_Report-2026"
        
        pbir_empty_file(self.test_dir, report_name)
        
        pbip_file = os.path.join(self.test_dir, f"{report_name}.pbip")
        assert os.path.exists(pbip_file)
    
    def test_content_replacement(self):
        """Test que le contenu est bien remplacé"""
        report_name = "CustomReport"
        
        pbir_empty_file(self.test_dir, report_name)
        
        # Lire le contenu du fichier .pbip
        pbip_file = os.path.join(self.test_dir, f"{report_name}.pbip")
        with open(pbip_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier que "Base" a été remplacé par le nouveau nom
        assert "Base" not in content
        assert report_name in content
    
    def test_folder_structure(self):
        """Test que la structure de dossiers est correcte"""
        report_name = "StructureTest"
        
        pbir_empty_file(self.test_dir, report_name)
        
        # Vérifier les fichiers essentiels
        essential_files = [
            f"{report_name}.pbip",
            f"{report_name}.Report/.platform",
            f"{report_name}.Report/definition.pbir",
            f"{report_name}.SemanticModel/.platform",
        ]
        
        for file_path in essential_files:
            full_path = os.path.join(self.test_dir, file_path)
            assert os.path.exists(full_path), f"Fichier manquant : {file_path}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
