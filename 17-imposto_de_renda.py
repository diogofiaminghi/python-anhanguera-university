salario = 0
salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"O colaborador isento de imposto.")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$ 142,80 de imposto.")
elif salario <= 3751.05:
    print(f"O colaborador deve pagar R$ 354,80 de imposto.")
elif salario <= 4664.68:
    print(f"O colaborador deve pagar R$ 636,13 de imposto.")
else:
    print(f"O colaborador deve pagar R$ 869,36 de imposto.")