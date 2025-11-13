# Exercício 02 - Adição de Comportamento (Métodos)

## Objetivo
Implementar métodos que alteram o estado de um objeto e métodos de consulta.

## Descrição do Exercício
Adicione à classe **Aluno** do exercício anterior os seguintes elementos:

### Requisitos:

1. Um atributo **notas** (uma lista de floats).

2. Um método `adicionar_nota(nota)` que insere uma nota na lista.

3. Um método `calcular_media()` que retorna a média das notas.

4. Um método `status()` que imprime "Aprovado" se a média for >= 7.0 e "Reprovado" caso contrário.

## Entrega
Crie um arquivo chamado `respExercicio02.py` com a implementação da classe Aluno aprimorada.

## Exemplo de Uso
```python
aluno = Aluno("João Silva", "2023001", "Engenharia de Software")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.2)
print(f"Média: {aluno.calcular_media()}")
aluno.status()
```

## Exemplo de Saída Esperada
```
Média: 8.23
Aprovado
```