'''
Combinations, Permutations e Product - Itertools
Combinaçao- Ordem nao importa
Permutaçao - ordem importa
Ambos nao repetem valores
Produtos - Ordem importa e repete valores unicos
'''
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
for grupo in product(pessoas, repeat=3):
    print(grupo)
