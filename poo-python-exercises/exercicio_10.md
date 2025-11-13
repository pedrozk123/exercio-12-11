# Exercício 10 - Jogo dos 7 Erros de POO em Python: A Modelagem Quebrada

## Objetivo
Identificar e corrigir falhas comuns de design e implementação em POO (Encapsulamento, Herança, Construtores).

## Descrição do Exercício
O código abaixo contém **7 erros** relacionados aos conceitos de Programação Orientada a Objetos. Sua tarefa é identificar todos os erros e corrigi-los.

## Código com Erros

```python
class pessoa:  # Erro 1
    def __init__(self, nome, idade):
        nome = nome  # Erro 2
        self.idade = idade
        self.__cpf = None  # Erro 3
    
    def apresentar():  # Erro 4
        return f"Olá, sou {self.nome}"

class Estudante(pessoa):
    def __init__(self, nome, idade, curso):
        self.nome = nome  # Erro 5
        self.idade = idade
        self.curso = curso
        self.notas = []
    
    def adicionar_nota(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)  # Erro 6

class Professor(pessoa):
    def __init__(self, nome, idade, departamento, salario):
        super().__init__(nome, idade)
        self.departamento = departamento
        self.salario = salario
    
    def apresentar(self):
        return f"Olá, sou o professor {self.nome} do departamento {self.departamento}"

# Testando o código
estudante = Estudante("João", 20, "Engenharia")
professor = Professor("Dr. Silva", 45, "Computação", 8000)

print(estudante.apresentar())
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")  # Erro 7
```

## Tarefa
1. **Identifique os 7 erros** no código acima
2. **Corrija todos os erros** 
3. **Teste o código corrigido** para garantir que funciona

## Entrega
Crie dois arquivos:
1. `Resposta_10.py` - com o código corrigido
2. `Resposta_10.md` - com um relatório dos erros encontrados e suas respectivas soluções

## Formato do Relatório
Para cada erro encontrado, descreva:
- **Erro X**: Descrição do problema
- **Solução**: Como foi corrigido
- **Conceito POO**: Qual princípio de POO estava sendo violado

## Dica
Os erros envolvem:
- Convenções de nomenclatura
- Inicialização de atributos
- Encapsulamento
- Definição de métodos
- Herança e uso de super()
- Tratamento de exceções
- Lógica de negócio