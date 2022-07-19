'''
Operadores logicos
and,or,not
in e not in
'''
'''
a = 2
b = 2
c = 3
print(a == b and b < c )             # comparaçao1 and comparaçao2 (verdadeiro e verdadeiro)= True
print(not a == b or not b < c)       # comparaçao1 and comparaçao2 (falso e verdadeiro)= False
print(not a == c and not b > a)
# comparaçao1 and comparaçao2 (verdadeiro e verdadeiro)= True
# comparaçao1 and comparaçao2 (falso e verdadeiro)= False

# or comp1 or comp2  #verdadeiro or verdadeiro
                     #(verdadeiro or falso)=true
'''
#not
'''
a=2
b = 3
if a <= b:
    print('a e menor ou igual a b')
elif b <= a:
    print('b e menor que a')'''

#in , not in
'''
nome = 'Gabriel'
if 'a' in nome:  # se existir 'a' dentro da variavel
    print(' a letra "A" esta no seu nome')
elif 'a' not in nome:  # se nao existir 'a' na variavel
    print("a letra 'u' nao esta no se nome")'''
#login
'''
login = input('Digite seu usuario ')
senha = input('Digite sua senha ')

senha1="13412"
login1='Gabriel@gmail.com'

if login == login1 and senha == senha1:
    print('Voce esta logado')
else:
    print('Usuario ou senha incorreto,'
          'tente novamente')
'''
n = 0
n2 = 0

if not n != n:
    print('Retorno 1')
else:
    print('Retorno 2')



