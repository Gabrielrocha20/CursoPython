'''
Enumerate - enumerar elementos da lista
'''
lista = [
    ['Edu','Joao','Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'ED', 'Lu']]
enumerada = list(enumerate(lista))
#print(enumerada[0][1][0])
'''     0      1        2
[(0, ['Edu', 'Joao', 'Luiz']),
     
(1, ['Maria', 'Aline', 'Joana']), 

(2, ['Helena', 'ED', 'Lu'])]  

esses parentezes sao tuplas
voce nao pode adicionar nem remover nada 
'''
for v1 in enumerate(lista):
    valorenumerado, minhalista = v1
    nome1, nome2, nome3 = minhalista
    print(nome3)      # desempacotamento de lista