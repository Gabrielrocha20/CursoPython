import random
import string

#inteiro = random.randint(10, 20)

inteiro = random.randrange(900, 1000, 10)
#flutuante = random.uniform(10, 20)
flutuante = random.random()
lista = ['Luiz', 'Otavio', 'Maria', 'Rose']
# sorteio = random.sample(lista, k=2)
# sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2)
random.shuffle(lista)

# gera senha

letra = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*'
geral = letra + digitos + caracteres
senha = ''.join(random.choices(geral, k=20))
print(senha)