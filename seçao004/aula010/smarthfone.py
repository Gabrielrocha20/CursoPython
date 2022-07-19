from eletronico import Eletronico
from log import LogMixin

class Smarthfone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado'
            print(info)
            self.log_error(info)
            return
        if self._conectado:
            error = f'{self._nome} JA ESTA CONECTADO'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} ESTA CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTA CONECTADO'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} foi desligar com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False
