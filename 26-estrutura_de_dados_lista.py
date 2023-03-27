#Objetos do tipo sequência: texto, listas e tuplas.
#Objetos do tipo set (conjunto).
#Objetos do tipo mapping (dicionário).
#Objetos do tipo array NumPy.

frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas) # True
print("abacate" in frutas) # False
print("abacate" not in frutas) # True
print(min(frutas)) # banana
print(max(notas)) # 10
print(frutas.count("maça")) # 2
print(frutas + notas)
print(2 * frutas)