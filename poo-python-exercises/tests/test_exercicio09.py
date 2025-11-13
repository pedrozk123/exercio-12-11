import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio09(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio09
            self.module = respExercicio09
        except ImportError:
            self.fail("Arquivo respExercicio09.py não encontrado")
    
    def test_aluno_apresentar(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        apresentacao = aluno.apresentar()
        self.assertIn("aluno", apresentacao.lower())
        self.assertIn("João", apresentacao)
        self.assertIn("Engenharia", apresentacao)
    
    def test_professor_apresentar(self):
        professor = self.module.Professor("Dr. Maria", "Computação", 8000)
        apresentacao = professor.apresentar()
        self.assertIn("professor", apresentacao.lower())
        self.assertIn("Dr. Maria", apresentacao)
    
    def test_funcionario_apresentar(self):
        funcionario = self.module.Funcionario("Carlos", "123", "01/01/1980", "Secretário", 3000)
        apresentacao = funcionario.apresentar()
        self.assertIn("funcionário", apresentacao.lower())
        self.assertIn("Carlos", apresentacao)

if __name__ == '__main__':
    unittest.main()