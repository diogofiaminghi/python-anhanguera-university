#Objetos do tipo sequência: texto, listas e tuplas.
#Objetos do tipo set (conjunto).
#Objetos do tipo mapping (dicionário).
#Objetos do tipo array NumPy.

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")