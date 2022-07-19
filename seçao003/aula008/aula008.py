import sys
import time
'''
Iteraveis
Iteradores
Geradores
'''
'''def gera():

    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
for v in g:
    print(v)'''
lista = [x for x in range(1000)]
lista1 = (x for x in range(1000))
for v in lista1:
    print(v)



