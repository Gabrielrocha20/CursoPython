"""
EM PYTHON TUDO E UM OBJETO: incluindo classes
Metaclasses  são as 'classes' que criam classes
type é uma metaclasse(!!!???)
"""


'''class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobreescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


class C(A):
    attr_classe = 'Valor C'


b = B()
print(b.attr_classe)'''

A = type(
    'A',
    (),
    {
        'attr': 'Ola mundo'
    }
)

a = A()
print(a)
