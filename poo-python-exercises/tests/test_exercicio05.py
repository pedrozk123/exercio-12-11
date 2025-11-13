import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio05(unittest.TestCase):
    def setUp(self):
        try:
            import respExercicio05
            self.module = respExercicio05
        except ImportError:
            self.fail("Arquivo respExercicio05.py não encontrado")
    
    def test_funcionario_herda_pessoa(self):
        funcionario = self.module.Funcionario("Ana", "111", "20/03/1988", "Coordenadora", 4500)
        self.assertIsInstance(funcionario, self.module.Pessoa)
        self.assertEqual(funcionario.nome, "Ana")
        self.assertEqual(funcionario.salario, 4500)
    
    def test_metodo_exibir_dados(self):
        funcionario = self.module.Funcionario("Ana", "111", "20/03/1988", "Coordenadora", 4500)
        self.assertTrue(hasattr(funcionario, 'exibir_dados'), "Método exibir_dados não encontrado")

if __name__ == '__main__':
    unittest.main()