# Exercício 07 - Agregação e Relacionamentos Muitos-Para-Muitos

## Objetivo
Modelar um relacionamento onde objetos existem independentemente, mas se referenciam mutuamente.

## Descrição do Exercício
Modifique as classes **Aluno** e **Disciplina** para implementar um relacionamento muitos-para-muitos.

### Requisitos:

1. **Aluno** deve ter um atributo `disciplinas_inscritas` (uma lista de objetos Disciplina).

2. **Disciplina** deve ter um atributo `alunos_matriculados` (uma lista de objetos Aluno).

3. Crie uma classe **Secretaria** com um método estático `inscrever_aluno(aluno, disciplina)` que:
   - Adicione o aluno na lista de alunos matriculados da disciplina
   - Adicione a disciplina na lista de disciplinas inscritas do aluno

4. Adicione métodos para listar as disciplinas de um aluno e os alunos de uma disciplina.

## Entrega
Crie um arquivo chamado `respExercicio07.py` com a implementação do relacionamento muitos-para-muitos.

## Exemplo de Uso
```python
aluno1 = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno2 = Aluno("Maria Santos", "2023002", "Ciência da Computação")
disciplina1 = Disciplina("POO", "POO001", 60)
disciplina2 = Disciplina("Banco de Dados", "BD001", 80)

Secretaria.inscrever_aluno(aluno1, disciplina1)
Secretaria.inscrever_aluno(aluno1, disciplina2)
Secretaria.inscrever_aluno(aluno2, disciplina1)

aluno1.listar_disciplinas()
disciplina1.listar_alunos()
```