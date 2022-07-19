'''
-> E uma lista de listas de numeros inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contem numeros entre 1 a 10 e eles podem ser duplicados
'''
#Exercicio
'''
-> Crie uma fncao que encontra o primeiro duplicado considerando o segundo numero como a duplicaçao.
    Requisitos:
        A ordem do numero duplicado e considerada a partir da segunda ocorrencia(o numero duplicado en si)
        Exemplo: [1, 2, 3, ->3<- , 2, 1]3
        se nao encontrar duplicados na lista retorn -1
'''
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],]


def clone(param_lista):
    numerochecado = set()
    primeiro_duplicado = -1

    for numero in param_lista:
        if numero in numerochecado:
            primeiro_duplicado = numero
            break

        numerochecado.add(numero)

    return primeiro_duplicado
for lista in lista_de_listas_de_inteiros:
    print(lista, 'numero duplicado', clone(lista))