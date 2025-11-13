import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio06(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio06
            self.module = respExercicio06
        except ImportError:
            self.fail("Arquivo respExercicio06.py não encontrado")
    
    def test_curso_tem_disciplinas(self):
        curso = self.module.Curso("Engenharia", "ES001")
        self.assertTrue(hasattr(curso, 'disciplinas'), "Atributo disciplinas não encontrado")
        self.assertIsInstance(curso.disciplinas, list)
    
    def test_adicionar_disciplina(self):
        curso = self.module.Curso("Engenharia", "ES001")
        disciplina = self.module.Disciplina("POO", "POO001", 60)
        curso.adicionar_disciplina(disciplina)
        self.assertIn(disciplina, curso.disciplinas)
    
    def test_carga_horaria_total(self):
        curso = self.module.Curso("Engenharia", "ES001")
        disciplina1 = self.module.Disciplina("POO", "POO001", 60)
        disciplina2 = self.module.Disciplina("BD", "BD001", 80)
        curso.adicionar_disciplina(disciplina1)
        curso.adicionar_disciplina(disciplina2)
        self.assertEqual(curso.carga_horaria_total(), 140)

if __name__ == '__main__':
    unittest.main()