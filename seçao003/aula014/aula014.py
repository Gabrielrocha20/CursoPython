'''
Try
Except
'''

try:
    a = 0
    try:
        a = 1/0
    except:
        print('erro')
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError) as erro:
    print('Erro de indice')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    pass
finally:
    a = 'aa'
print(a)
print('bora continuar...')