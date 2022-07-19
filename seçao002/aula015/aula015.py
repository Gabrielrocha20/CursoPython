'''
Manipulando strings
* String indices
* Fatiamentos de string [inicio;fim;passo]
* Funçoes built-in len, abs, type, print, etc...
 Essas funçoes podem ser usadas diretamente em cada tipo

 voce pode conferir tudo isso em
 https://docs.python.org/3/library/stdtypes.html
 https://docs.python.org/3/library/functions.html
'''
# positivos   [012345678]
texto       = 'python s2'
print(texto[6])
#print( texto[9]) nao existe

# negativos  -[987654321]
url = 'www.google.com.br/'
#print( url[:-1] ) o ultimo caractere e cortado
nova = texto[2:6] # o 2 antes dos : ele tira tudo antes  e depois de dois pontos ele tira tudo depois de 6 caracteres
print(nova)
# nova=texto[0:6:2] 0 e o orimeiro caractere , 6 e outro caractere e o 2 significa q vai ler do 0 ao 6 pulando de 2 em2