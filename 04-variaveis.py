# MODO 1 - USANDO FORMATADORES DE CARACTERES

nome = input("Digite seu nome: ")
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" %(nome))

# MODO 2 - USANDO A FUNÇÃO format() PARA IMPRIMIR VARIÁVEL E TEXTO

print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world" .format(nome))

# MODO 3 - USANDO STRINGS FORMATADAS

print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")