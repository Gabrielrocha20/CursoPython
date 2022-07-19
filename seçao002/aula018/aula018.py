'''
For in em Python
iterando strings com for
Função range (start = 0, stop, step=1)
'''
texto = 'python'
ns = ''
'''
c = 0
while c < len(texto):
    print(texto[c])
    c += 1'''
'''
for n , letra in enumerate (texto):
    print(n, letra)'''

'''for n in range(20, 10, -2):
    print(n)'''
'''for n in range (100):
    if n % 8 == 0:
        print(n)'''
for letra in texto:
    if letra == 't':
        #continue
        ns = ns + letra.upper()
    elif letra == 'h':
        ns += letra.upper()
        break
    else:
        ns  += letra
print(ns)