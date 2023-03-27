quantidade_de_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if quantidade_de_faltas <= 5 and media_final >=7:
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")