def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui
    return False # Se chegar até aqui, significa que o valor não foi encontrado

lista = list(range(1, 50))

print(lista)

print('\n',executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))

#1-Encontra o item no meio da sequência.
#2-Se o valor procurado for igual ao item do meio, a busca encerra.
#3-Se não, verifica se o valor buscado é maior ou menor que o valor central.
#4-Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada), se não for maior, a busca acontecerá na metade inferior da sequência (a superior é descartada).
#4-Repete os passos: 1, 2, 3, 4.