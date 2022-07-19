'''
1- Crie uma função que exibe uma saudação com os parametros saudação e nome.

def saudacao(saudação, nome):
    print(saudação, nome)

saudacao('Olá', 'Gabriel')
'''
'''
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles

def soma(n1, n2, n3):
    print(n1 + n2 + n3)
soma(8, 5, 2)'''
'''
3 - Crie uma função que receba 2 números.O primeiro é um valor eo segundo um percentual
(ex.10%). Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo.

def calculo(n1, n2):
    return n1 + (n2 / 100) * n1
soma = calculo(150, 15)
print(soma)'''
'''
4 - Fizz Buzz - se o parâmetro da função for divisível por 3, retorn fizz, se o parâmetro da função for divisivel por 5
retorn buzz. Se o parâmetro da função for divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o numero 
enviado
'''
def divisao(n1):
    if n1 % 3 ==0 and n1 % 5 == 0:
        return'FizzBuzz'
    if n1 % 3 == 0:
        return'Fizz'
    if n1 % 5 == 0:
        return'Buzz'
    return n1

print(divisao(10))
print(divisao(3))
print(divisao(15))
print(divisao(17))