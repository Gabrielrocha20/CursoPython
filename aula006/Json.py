"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation)  e um formato de troca de dados entre sistemas e proframas muito leve e de
facil utilizacao Muito utilizado por APIs

DUMPS / Dump
##########################
Python                 JSON
dict                   object
list,tuple             array
str                    string
int,float              number
True                   true
False                  false
None                   null

LOADS / Load
############################
JSON                Python
object              dict
array               list
string              str
number (int)        int
number (real)       float
true                True
false               False
null                None
"""

from dados import *
import json

'''dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)'''

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)
