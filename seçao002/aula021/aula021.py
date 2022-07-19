'''
Split,Join,Enumerate em python
*Split - dividir uma string #str
*Join - juntar uma lista # str
* Enumerate - enumerar elementos da lista # iteraveis
'''
'''
string = 'O Brasil e o o o pais do futebol, o Brasil e penta'
lista1 = string.split(' ')
lista2 = string.split(',')
palavra = ''
contagem = 0
for valor in lista2:
    print(valor.strip().capitalize())
    # print(f'a palavra {valor} apareceu {lista1.count(valor)}x')
    qtd = lista2.count(valor)
    if qtd > contagem:
        contagem = qtd
        palavra = valor
print(f'a palavra que apareceu mais vezes e {palavra}({contagem}x)')
'''
'''
string = 'O Brasil e penta'
lista = string.split(' ')
string2 = ','.join(lista)
print(string)
print(lista)
print(string2) '''
'''string = 'O Brasil e penta'
lista = string.split(' ')
for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])'''
'''lista = ['Gabriel','Milena','Valber']               

for indice, nome in enumerate(lista):
    print(indice, nome)'''
lista = ['Gabriel','Milena','Valber']
n1, n2, n3 = lista
print(n2)                         # desenpacotamento de lista