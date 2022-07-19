'''
while em Python
utilizando para realizar ações enquanto
uma condiçao for verdadeira

Requisitos:entender condições e operadores
'''
'''while True:  # enquanto essa condiçao for verdadeira.. faça
    nome = input('Qual e o seu nome? ')
    print(f' Ola {nome}')

print('nao sera executada')'''

x = 0
while x < 10:
    if x ==3:  #quando chegar a 3 ele vai parar e vai fica em um loop
        x = x + 1  #assim ele vai pular o 3 e vai continuar ate chegar a 10
        #continue
        break           # na hora q chegar em 3 ele finaliza o codigo
    print(x)
    x = x + 1