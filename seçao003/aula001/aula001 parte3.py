'''
Funções (def) em python - *args **kwargs
parte 3
'''
'''def func(a1,a2, a3, a4, a5, nome=None, a6=None):        #se utilizar um argumento com valor padrao,todos depois pricisa
    print(a1, a2, a3, a4, a5, nome, a6)
var = func(1, 2, 3, 4, 5, nome='Gabriel', a6='5')
print(var)'''
'''def func(*args):
    print((args))
lista = [1,2,3,4,5]
print(*lista, sep='-')'''
'''def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
func(1,2,3,4,5)'''
'''def func(*args):
    args[0] = 20       # da erro pq n se pode alterar uma tupla
    print(args)
func(1,2,3,4,5)'''
def func(*args, **kwargs):
    '''args = list(args)
    args[0] = 20
    print(args)'''
    '''for v in args:
        print(v)'''
    print(args)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Gabriel', sobrenome='Miranda', idade=30)