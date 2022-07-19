from time import sleep
from threading import Thread, Lock

"""class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 7)
t1.start()
t2 = MeuThread('Thread 2', 3)
t2.start()
t3 = MeuThread('Thread 3', 4)
t3.start()
t4 = MeuThread('Thread 4', 5)
t4.start()

for i in range(20):
    print(i)
    sleep(1)
"""


"""def vai_demora(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demora, args=('Olá mundo', 5))
t.start()

while t.is_alive():
    print('Esperando a thread')
    sleep(2)

print('A thread acabou')"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print(f'Não temos {quantidade} ingressos para vender!')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque} em estoque')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    threads = []
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)
    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break