# Exercício 09 - Polimorfismo (Diferentes Formas)

## Objetivo
Demonstrar como diferentes objetos respondem de maneiras únicas ao mesmo método.

## Descrição do Exercício
Implemente polimorfismo através do método `apresentar()` em diferentes classes.

### Requisitos:

1. Certifique-se de que as classes **Aluno**, **Professor** e **Funcionario** possuem o método `apresentar()`.

2. Cada classe deve implementar o método de forma específica:
   - **Aluno**: deve dizer "Olá, sou o aluno [nome] e estudo no curso [curso]."
   - **Professor**: deve dizer "Olá, sou o professor [nome] e leciono no departamento [departamento]."
   - **Funcionario**: deve dizer "Olá, sou o funcionário [nome] e meu cargo é [cargo]."

3. Crie uma lista contendo objetos de Aluno, Professor e Funcionario.

4. Percorra a lista e chame o método `apresentar()` para cada objeto, demonstrando polimorfismo.

## Entrega
Crie um arquivo chamado `respExercicio09.py` com a implementação do polimorfismo.

## Exemplo de Uso
```python
pessoas = [
    Aluno("João Silva", "2023001", "Engenharia de Software"),
    Professor("Dr. Maria", "Computação", 8000.0),
    Funcionario("Carlos Santos", "123.456.789-00", "01/01/1980", "Secretário", 3000.0)
]

for pessoa in pessoas:
    print(pessoa.apresentar())
```

## Exemplo de Saída Esperada
```
Olá, sou o aluno João Silva e estudo no curso Engenharia de Software.
Olá, sou o professor Dr. Maria e leciono no departamento Computação.
Olá, sou o funcionário Carlos Santos e meu cargo é Secretário.
```