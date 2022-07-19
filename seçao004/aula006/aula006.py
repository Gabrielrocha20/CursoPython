from classes import Escritor, Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('Joaozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
del escritor
