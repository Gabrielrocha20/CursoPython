'''
Setter =  configurando um valor (=)
Getter =  Obter um valor (.)
'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome


p1 = Pessoa('Otavio')

print(p1.nome)