lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]
d1 = {f'chave{x}': x**2 for x in range(5)}
print(d1)