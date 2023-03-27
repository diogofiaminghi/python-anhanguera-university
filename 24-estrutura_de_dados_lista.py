#Objetos do tipo sequência: texto, listas e tuplas.
#Objetos do tipo set (conjunto).
#Objetos do tipo mapping (dicionário).
#Objetos do tipo array NumPy.

vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')