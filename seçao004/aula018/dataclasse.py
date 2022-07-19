"""
O que sãp dataclasses? O modulo Dataclasse fornece um decorador e funçoes
para criar automaticamente metodos, como __init__(), __repr__(), __eq__(etc)
em classes definidas pelo usuario
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmenteee descrito na PEP 557
Adicionado na versao 3.7 do Python

"""

from dataclasses import dataclass, field


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome : str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(f'Invalid type {type(self.nome).__name__} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('D', '4')
p4 = Pessoa('B', '6')

pessoas = [p1, p2, p3, p4]
print(sorted(pessoas, key=lambda  pessoa: pessoa.sobrenome, reverse=True))