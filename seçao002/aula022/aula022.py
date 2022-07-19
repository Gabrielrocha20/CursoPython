'''
Desempacotamento de listas python
'''
lista = ['luiz', 'joao', 'maria']
# n1, n2, *outra_lista = lista
*outra_lista, n1 = lista
print(outra_lista)
