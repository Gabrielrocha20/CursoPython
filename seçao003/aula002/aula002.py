'''def funcao(arg, arg2):
    return arg * arg2
var = funcao(2,2)
a = lambda x, y: x * y  # isso aki seria a mesma coisa do q a def acima
print(a(2, 2))'''
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
'''def func(item):  teria q ser feito assim 
    return item[1]'''

'''lista.sort(key=lambda item: item[1]) com lambda fica assim , mas pode simplificar ainda mais
print(lista)'''
print(sorted(lista, key=lambda i: i[1], reverse=True))