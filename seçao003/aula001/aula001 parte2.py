'''
Funções (def) em Python - return
'''
def funcao(var):
    # print(var)
    #return var  #retorna o valor,nao passa daqui
    print('isso nao sera executado')
    return var  # aqui o print vai aparecer pq ele ta antes do retorno
variavel = funcao('Valor que eu quero')
if variavel:
    print(variavel)
else:
    print('Nenhum valor')
'''def divisao(n1, n2):
    if n2 == 0:
        return 
    return n1 / n2
divide =  divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta invalida.')'''
'''def f(var):
    print(var)
def dumb():
    return f
var = dumb()
var('Pode imprimir isso na tela pq ele tem a funçao de f')'''
'''def dumb():
    return('Luiz', 'Otavio')
var = dumb()
print(var, type(var))'''