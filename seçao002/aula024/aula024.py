'''
Operador ternario em python
'''
'''logged_user = False
msg = 'Usuario logado.' if logged_user == True else 'Usuario precisa logar'
#if checa a condiçao e se for verdadeiro ele fala que esta logado se nao for da else
print(msg)'''
idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Voce precisa digitar apenas numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Nao pode acessar'
    print(msg)
'''if idade >= 18:
    print('Pode acessar')
else:
    print('Nao pode acessar')'''

