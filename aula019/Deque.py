"""
Pilhas  e filas
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que sao adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os indices serao modificados.
"""

"""livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

livro_removido = livros.pop()"""

from collections import deque
from time import sleep

fila = deque(maxlen=10)
fila.
'''for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)'''
'''fila.append('Joao')
fila.append('Maria')
fila.append('Gabriel')
fila.append('milena')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
for nome in fila:
    print(nome)'''