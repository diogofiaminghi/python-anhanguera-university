import pandas as pd

print("PRIMEIRO EXERCICIO")
print(pd.Series(data=5)) # Cria uma Series com o valor a

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

print("SEGUNDO EXERCICIO")
print(pd.Series(lista_nomes)) # Cria uma Series com uma lista de nomes

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}

print("TERCEIRO EXERCICIO")
print(pd.Series(dados)) # Cria uma Series com um dicionário

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

print("QUARTO EXERCICIO")
print(pd.Series(lista_nomes, index=cpfs))

print("QUINTO EXERCICIO")

series_dados = pd.Series(lista_nomes, index=cpfs)

print(series_dados.loc['111.111.111-11'])

