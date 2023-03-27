#Objetos do tipo sequência: texto, listas e tuplas.
#Objetos do tipo set (conjunto).
#Objetos do tipo mapping (dicionário).
#Objetos do tipo array NumPy.

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)