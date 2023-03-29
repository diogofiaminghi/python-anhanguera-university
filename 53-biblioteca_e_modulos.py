#IMPORTA O MODULO INTEIRO PARA A MEMORIA
import math

print(math.sqrt(25)) #modulo.nome_do_item
print(math.log2(1024))
print(math.cos(45))

#IMPORTA O MODULO INTEIRO PARA A MEMORIA COM UM ALIAS (APELIDO)
import math as m

m.sqrt(25) #apelido.nome_do_item
m.log2(1024)
m.cos(45)

#IMPORTA APENAS ITENS ESPECIFICOS DE UM MODULO
from math import sqrt, log2, cos

sqrt(25) #invocação direta da função
log2(1024)
cos(45)
