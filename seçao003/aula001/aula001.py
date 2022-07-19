'''
Funções - def em python (parte1)
'''
def saudacao(msg, nome):
    nome = nome.replace('o', '0')
    msg = msg.replace('o', '0')
    print(msg, nome)
saudacao('Ola','Luiz Otavio')
saudacao('Oi','Luiz Otavio')
saudacao('Ola','Gabriel')


