import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio07(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio07
            self.module = respExercicio07
        except ImportError:
            self.fail("Arquivo respExercicio07.py não encontrado")
    
    def test_aluno_tem_disciplinas_inscritas(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        self.assertTrue(hasattr(aluno, 'disciplinas_inscritas'))
        self.assertIsInstance(aluno.disciplinas_inscritas, list)
    
    def test_disciplina_tem_alunos_matriculados(self):
        disciplina = self.module.Disciplina("POO", "POO001", 60)
        self.assertTrue(hasattr(disciplina, 'alunos_matriculados'))
        self.assertIsInstance(disciplina.alunos_matriculados, list)
    
    def test_secretaria_inscrever_aluno(self):
        aluno = self.module.Aluno("João", "123", "Engenharia")
        disciplina = self.module.Disciplina("POO", "POO001", 60)
        self.module.Secretaria.inscrever_aluno(aluno, disciplina)
        self.assertIn(disciplina, aluno.disciplinas_inscritas)
        self.assertIn(aluno, disciplina.alunos_matriculados)

if __name__ == '__main__':
    unittest.main()