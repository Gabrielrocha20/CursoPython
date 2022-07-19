perguntas = {
    'pergunta 1':{
        'pergunta': 'Quanto e 2+2?',
        'respostas': {'a': '1',
                      'b': '4',
                      'c': '5',},
       'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto e 3x2?',
        'respostas': {'a': '4',
                      'b': '10',
                      'c': '6', },
        'resposta_certa': 'c',
    },
    'pergunta 3': {
        'pergunta': 'Quanto e 0.3x10?',
        'respostas': {'a': '30',
                      'b': '10',
                      'c': '3.0', },
        'resposta_certa': 'c',
    },
    'pergunta 4': {
        'pergunta': 'Quanto e 12x2?',
        'respostas': {'a': '34',
                      'b': '24',
                      'c': '18', },
        'resposta_certa': 'b',
    },
    'pergunta 5': {
        'pergunta': 'Quanto e 9x2?',
        'respostas': {'a': '18',
                      'b': '1.80',
                      'c': '17', },
        'resposta_certa': 'a',
    },

}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]:{rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('EBA VOCE ACERTOU')
        respostas_certas += 1
    else:
        print('IXI VOCE ERROU')
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas *100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')