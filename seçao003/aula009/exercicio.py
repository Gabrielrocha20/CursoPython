'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que outra, a soma so vai consideirar o tamanho da menos

Exemplo:
lista_a  = [1,2,3,4,5,6,7]
lista_b  = [1,2,3,4]

======================resultado
lista_soma = [2,4,6,8]
'''
from itertools import zip_longest
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

listasoma = [x + y for x, y in zip(lista_a, lista_b)]
print(listasoma)
'''for i in range(len(lista_b)):
    listasoma.append(lista_a[i] + lista_b[i])
print(listasoma)'''
'''for i, _ in enumerate(lista_b):
    listasoma.append(lista_a[i] + lista_b[i])
print(listasoma)'''
