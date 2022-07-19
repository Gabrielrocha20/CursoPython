n = input('digite um numero')
n2 = input('digite um numero')
#n = int(n)
#n2 = int(n2)
#print(n + n2)
# isnumeric isdigit isdecimal
#numeros e positivos(123456)inteiro
#print(n.isnumeric())
#print(n2.isnumeric())
'''
if n.isdigit()and n2.isdigit():
    n = int(n)
    n2 = int(n2)
    print(n + n2)
else:
    print('nao pude converter os numeros para realizar contas')

#quando a pessoa digitar 2.2 nmr flutuante n vai ir'''
try :
    n = float(n)
    n2 = float(n2)
    print('{:.0f}'.format(n + n2))
except:
    print('nao pude converter os numeros para realizar contas')