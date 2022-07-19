'''
count - Itertools / gera um contador que e um iterador
'''

from itertools import count

'''contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor,2))
    if valor >= 10:
        break'''

contador =  count()
lista = ['Luiz', 'Joao', 'Maria']

lista = zip(contador, lista)
print(list(lista))