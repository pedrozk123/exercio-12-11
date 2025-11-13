import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio08(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio08
            self.module = respExercicio08
        except ImportError:
            self.fail("Arquivo respExercicio08.py não encontrado")
    
    def test_criar_departamento_exatas(self):
        dept = self.module.Departamento.criar_departamento_exatas("Matemática")
        self.assertEqual(dept.sigla, "EXA")
        self.assertEqual(dept.nome, "Matemática")
    
    def test_criar_departamento_humanas(self):
        dept = self.module.Departamento.criar_departamento_humanas("Letras")
        self.assertEqual(dept.sigla, "HUM")
        self.assertEqual(dept.nome, "Letras")
    
    def test_departamento_tem_professores(self):
        dept = self.module.Departamento("Computação", "COMP")
        self.assertTrue(hasattr(dept, 'professores'))
        self.assertIsInstance(dept.professores, list)

if __name__ == '__main__':
    unittest.main()