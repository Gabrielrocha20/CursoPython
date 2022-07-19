'''
1 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada


def func1(funcao):
   return funcao

def func2():
    return'Gabriel'
ff = func1(func2())
print(ff)
'''
'''
2 - Crie uma função1 que recebe  uma função2 como parametro e retorn o valor da função2 executada
Faça a função1 executar duaas funções que recebam um número diferente de argumentos
'''
def master(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fnome(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

ex = master(fnome, 'Gabriel')
ex2 = master(saudacao, 'Gabriel', saudacao='Bom dia')
print(ex)
print(ex2)