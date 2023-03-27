#Objetos do tipo sequência: texto, listas e tuplas.
#Objetos do tipo set (conjunto).
#Objetos do tipo mapping (dicionário).
#Objetos do tipo array NumPy.

numeros = list(range(0, 21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)    