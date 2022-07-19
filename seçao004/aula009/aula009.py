from classes import *

'''
Associação - Usa | Agregação - Tem | Composição - E dono | Herança - E
'''

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()

print()

c2 = ClienteVIP('Rose', 25, 'Rocha')
c2.falar()