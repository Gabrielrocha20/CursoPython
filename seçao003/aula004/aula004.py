'''
Dicionario
'''
'''d1 =  {'chave1':'valor da chave'}
d1['nova_chave']= 'Valor da nova chave
d1 = dict(chave='Valor da chave', chave2='Valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'''
'''d1 = {
    'str' : 'valor',
    123  : 'outro valor',
    (1,2,3,4) : 'Tupla',
}'''
'''d1['naoexiste'] = 'Agora existe.'
if 'naoexiste' in d1:
    print(d1['naoexiste'])
print('Oi')'''
'''d1['nomedachave'] = 'Agora existe'
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))'''

'''del d1['str']'''
'''print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())'''
'''for k, v in d1.items():
    print(k, v)'''
'''clientes = {
    'cliente' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Otavio',
    },
    'cliente2' : {
        'nome' : 'Gabriel',
        'sobrenome' : 'Rocha'
    }
}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')'''
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Luiz', 'Otavio']}
v = copy.deepcopy(d1)
v['d'][0] = 'joao'
print(d1)
print(v)