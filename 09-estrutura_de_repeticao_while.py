# UTILIZAMOS O WHILE QUANDO NÃO SABEMOS QUANTAS VEZES O TRECHO DO CÓDIGO SERÁ EXECUTADO

numero = 1

while numero != 0:
    
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")