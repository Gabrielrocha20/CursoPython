'''
Map - mapea a lista completa
Filter -  filta coisas da lista tipo coisas maiores q 5 ou menores
reduce - soma todos os produtos da lista
'''
from dados import produtos, pessoas, lista
from functools import reduce
'''
#nova_lista = map(lambda x: x * 2, lista)
#nova_lista = [x * 2 for x in lista]
#print(list(nova_lista))
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p
novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p
nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)'''
'''nova_lista = filter(lambda x: x > 5, lista)
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))
def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True

nova_lista = filter(filtra, pessoas)
for pessoa in nova_lista:
    print(pessoa)'''

'''soma_lista = reduce(lambda ac, i: i + ac, lista , 0)
soma_precos = reduce(lambda ac, p:  p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))'''
soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idade / len(pessoas))