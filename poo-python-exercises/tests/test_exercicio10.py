import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExercicio10(unittest.TestCase):
    def setUp(self):
        try:
            import Resposta_10
            self.module = Resposta_10
        except ImportError:
            self.fail("Arquivo Resposta_10.py não encontrado")
    
    def test_classe_pessoa_maiuscula(self):
        self.assertTrue(hasattr(self.module, 'Pessoa'), "Classe Pessoa não encontrada")
    
    def test_estudante_herda_pessoa(self):
        estudante = self.module.Estudante("João", 20, "Engenharia")
        self.assertIsInstance(estudante, self.module.Pessoa)
        self.assertEqual(estudante.nome, "João")
    
    def test_calcular_media_sem_divisao_zero(self):
        estudante = self.module.Estudante("João", 20, "Engenharia")
        media = estudante.calcular_media()
        self.assertEqual(media, 0)
    
    def test_metodo_apresentar_tem_self(self):
        pessoa = self.module.Pessoa("João", 20)
        apresentacao = pessoa.apresentar()
        self.assertIn("João", apresentacao)

if __name__ == '__main__':
    unittest.main()