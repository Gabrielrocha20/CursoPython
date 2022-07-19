'''
Herança
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f'{self.nomeclasse} Esta Falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Esta Comprando ...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} Esta Estudando ...')'''

'''

'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Esta Falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Esta Comprando ...')

    def falar(self):
        print('Estou em cliente')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')