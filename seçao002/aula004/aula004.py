'''
str - strings 'palavras dentro de aspas'
int - numero inteiro  123456 -10 -20 100000
float - numeros reais/flutuantes 1.5 1.4 5.4 45.89899
bool - valor boleano/logico True/False 10==10
'''
'''
print('Luiz', type('Luiz'))  # str
print('10', type('10'))  # str tbm por que esta dentro de aspas
print(10, type(10))  # int
print(10.34, type(10.34))  # float
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))  # boleano compara se e verdade ou falso
print('Luiz', type('Luiz'), bool('luiz')) # so boll tiver assim '' e tiver vazio ele da como false
                                          #Luiz <class 'str'> True
print('10', type('10'), type(int('10')))  #10 <class 'str'> <class 'int'>'''
print('Meu nome e gabriel', type('meu nome e gabriel'))
print('Minha idade e', int(20), type(20))
print('Minha altura e', float(1.72), type(1.72))
print('Eu sou maior de idade=', bool(20 >= 18), type(20 >= 18))