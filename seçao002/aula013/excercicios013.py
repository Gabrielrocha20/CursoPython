'''
Faça um programa que peça ao usuario para digitar um numero inteiro
informe se este número é par ou ímpar.Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. EX
Bom dia 0-11, boa tarde 12-17 e Boa noite 18-23
'''

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 "Seu nome é muito grande"'''
'''
print('A baixo fale um numero para saber se ele e impar ou par')
n = input('Digite um numero ')

try:
    n1 = int(n) % 2
    if n1 == 1:
        print('Esse numero é impar')
        r2 = input('Caso você quiser repetir digite "sim" se nao digite "não"')
        if r2 == 'sim':
            print('A baixo fale um numero para saber se ele e impar ou par')
            n = input('Digite um numero ')

            try:
                n1 = int(n) % 2
                if n1 == 1:
                    print('Esse numero é impar')

                else:
                    print('Esse numero é par')
            except:
                print('Não foi possivel, A resposta informada '
                      'por você nao atende os requisitos para somar ')
                print('Tente novamente')
                r = input('Você quer recomeçar? se sim digite sim , se nao digite não ')
        elif r2 == 'nao':
            print('ATE MAIS')

    else:
        print('Esse numero é par')
        r2 = input('Caso você quiser repetir digite "sim" se nao digite "não"')
        while r2 == 'sim':
            print('A baixo fale um numero para saber se ele e impar ou par')
            n = input('Digite um numero ')

            try:
                n1 = int(n) % 2
                if n1 == 1:
                    print('Esse numero é impar')

                else:
                    print('Esse numero é par')
            except:
                print('Não foi possivel, A resposta informada '
                      'por você nao atende os requisitos para somar ')
                print('Tente novamente')
                r = input('Você quer recomeçar? se sim digite sim , se nao digite não ')
except:
    print('Não foi possivel, A resposta informada '
          'por você nao atende os requisitos para somar ')
    print('Tente novamente')
    r = input('Você quer recomeçar? se sim digite sim , se nao digite não ')
    while r == 'sim':
        print('A baixo fale um numero para saber se ele e impar ou par')
        n = input('Digite um numero ')

        try:
            n1 = int(n) % 2
            if n1 == 1:
                print('Esse numero é impar')
                r = input('Você quer recomeçar? se sim digite sim , se nao digite não ')

            else:
                print('Esse numero é par')
                r = input('Você quer recomeçar? se sim digite sim , se nao digite não ')
        except:
            print('Não foi possivel, A resposta informada '
                  'por você nao atende os requisitos para somar ')
            print('Tente novamente')
    else:
        print('ATE MAIS')'''
"""
print('A baixo me diga as horas e depois os minutos ')
print('EX:me informe as horas:13')
print('EX:me informe os minutos:23')
h = input('Ola Joven, meu relogio quebrou poderia me informar as horas')
m = input('Me informe o minuto')
try:
    h1 = int(h)
    num = 12
    num2 = 17
    if h1 <= 11:
            print('Bom Dia')
    if h1 <= 17 :
        print('Boa tarde')
    if h1 <= 23:
        print('boa noite')
    else:
        print('tente novamete')
        rr = input('Digite sim se quiser tentar novamente, digite nao se nao quiser')
        if rr == 'sim':
            print('A baixo me diga as horas e depois os minutos ')
            print('EX:me informe as horas:13')
            print('EX:me informe os minutos:23')
            h = input('Ola Joven, meu relogio quebrou poderia me informar as horas')
            m = input('Me informe o minuto')
            try:
                h2 = int(h)

                if h2 <= 11:
                    print('Bom Dia')
                if h2 >= 12 and h2 <= 17:
                    print('Boa tarde')
                if h2 >= 18 and h2 <= 23:
                    print('boa noite')
                else:
                    print('tente novamete')
                    rrr = input('Digite sim se quiser tentar novamente, digite nao se nao quiser')
                    if rrr == 'sim':
                        print('A baixo me diga as horas e depois os minutos ')
                        print('EX:me informe as horas:13')
                        print('EX:me informe os minutos:23')
                        h = input('Ola Joven, meu relogio quebrou poderia me informar as horas')
                        m = input('Me informe o minuto')
                    else:
                        print('ATE MAIS')

            except:
                print('tente novamente')
                t = input('Você quer tentar novamente?se sim digite sim ')
                if t == 'sim':
                    print('A baixo me diga as horas e depois os minutos ')
                    print('EX:me informe as horas:13')
                    print('EX:me informe os minutos:23')
                    h = input('Ola Joven, meu relogio quebrou poderia me informar as horas')
                    m = input('Me informe o minuto')
                    try:
                        h1 = int(h)
                        num = 12
                        num2 = 17
                        if h1 <= 11:
                            print('Bom Dia')
                        if h1 >= 12 and h1 <= 17:
                            print('Boa tarde')
                        if h1 >= 18 and h1 <= 23:
                            print('boa noite')
                    except:
                        print('tente novamente')
                        t = input('Você quer tentar novamente?se sim digite sim ')
                else:
                    print('Até mais')
        else:
            print('ATE MAIS')

except:
    print('tente novamente')
    t = input('Você quer tentar novamente?se sim digite sim ')
    if t == 'sim':
        print('A baixo me diga as horas e depois os minutos ')
        print('EX:me informe as horas:13')
        print('EX:me informe os minutos:23')
        h = input('Ola Joven, meu relogio quebrou poderia me informar as horas')
        m = input('Me informe o minuto')
        try:
            h1 = int(h)
            num = 12
            num2 = 17
            if h1 <= 11:
                print('Bom Dia')
            if h1 >= 12 and h1 <= 17:
                print('Boa tarde')
            if h1 >= 18 and h1 <= 23:
                print('boa noite')
        except:
            print('tente novamente')
            t = input('Você quer tentar novamente?se sim digite sim ')
    else:
        print('Até mais')"""
u = input('Me diga seu nome de usuario ')
u1 = len(u)
if u1 <= 4:
    print('seu nome e muito pequeno')
if u1 >= 5 and u1 <= 6:
    print('seu nome e normal')
if u1 > 6:
    print('seu nome e muito grande')





