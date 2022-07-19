'''
 1 Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

n = [1, 2, 3, 4, 5]
for valor in n:
    print(valor)'''
'''
 2 Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no = n[10:0:-1]
print(no)'''
'''
 3Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

d = []
i = 1
while i <= 4:
    print('Descubra sua media')
    n = float(input('Digite uma nota '))
    d.append(n)
    i += 1
lists = sum(d) / 4
print( 'esta e sua media {}'.format(lists))'''
'''
 4Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
 
d = ['gabriel','valber','vayne','milena','claudia','maria','samuel','juliana','duda','bete']
for v in enumerate(d):
    print(v.strip().capitalize())'''
'''
 5Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
 números IMPARES no vetor impar. Imprima os três vetores.
 '''
'''
 6Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o 
 número de alunos com média maior ou igual a 7.0.
 '''
'''
 7Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
 '''
'''
 8Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
 Imprima a idade e a altura na ordem inversa a ordem lida.
 '''
'''
 9Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados 
 dos elementos do vetor.
 '''
'''
 10Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
 cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''

'''print('sequencia de fibonacci ')
n = int(input('digite o numero e voce vai ver a sequencia de fibonacci '))
n1 = n + n
n2 = n1 + n
n3 = n2 + n1
n4 = n3 + n2
n5 = n4 + n3
n6 = n5 + n4
n7 = n6 + n5
n8 = n7 + n6
n9 = n8 + n7
n10 = n9 + n8
n11 = n10 + n9
n12 = n11 + n10
n13 = n12 + n11
n14 = n13 + n12
n15  = n14 + n13
n16 = n15 + n14
n17 = n16 + n15
print(n)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)'''

print('Sequencia de fibonacci')
i = 1
i2 = 0
i3 = 0
while i <=144:
    print(i)
    i3 = i
    i = i + i2
    i2 =i3

