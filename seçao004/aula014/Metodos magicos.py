"""
https://rszalski.github.io/magicmethods/
"""


class A:
    '''def __new__(cls, *args, **kwargs):
        ]def haha(*args, **kwargs):
            print('Fala OI')
        cls.haha = haha]
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste'''

    def __init__(self):
        print('EU SOU INIT')

    '''def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado'''

    def __setattr__(self, key, value):
        self.__dict__[key] = value


a = A()
a.nome = 'Luiz Otavio'
print(a.nome)