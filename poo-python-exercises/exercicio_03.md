# Exercício 03 - Encapsulamento e Propriedades

## Objetivo
Aplicar o princípio do Encapsulamento usando getters e setters (ou @property).

## Descrição do Exercício
Crie a classe **Professor** aplicando conceitos de encapsulamento.

### Requisitos:

1. O atributo **salario** deve ser privado (usando `_salario`).

2. Implemente um método getter para salario (ou use `@property`).

3. Implemente um método setter para salario que só permita a alteração se o novo valor for positivo. Caso contrário, imprima uma mensagem de erro e mantenha o valor anterior.

4. Adicione outros atributos básicos como nome e departamento.

## Entrega
Crie um arquivo chamado `respExercicio03.py` com a implementação da classe Professor.

## Exemplo de Uso
```python
prof = Professor("Dr. Silva", "Computação", 5000.0)
print(f"Salário atual: R$ {prof.salario}")
prof.salario = 6000.0  # Deve funcionar
print(f"Novo salário: R$ {prof.salario}")
prof.salario = -1000.0  # Deve dar erro
print(f"Salário após tentativa inválida: R$ {prof.salario}")
```

## Exemplo de Saída Esperada
```
Salário atual: R$ 5000.0
Novo salário: R$ 6000.0
Erro: Salário deve ser um valor positivo!
Salário após tentativa inválida: R$ 6000.0
```