#complexidade O(N2) - algoritmos lentos, mas fáceis de entender
    #selection sort
    #bubble sort
    #insertion sort
    
#complexidade O(N log N) - algoritmos com performance superior, mas mais complexo de entender
    #merge sort
    #quick sort
    
#MERGE SORT - dividir para conquistar

#ETAPA DA DIVISAO
#1-Com base na lista original, encontre o meio e separe-a em duas listas: esquerda_1 e direita_2.
#2-Com base na sublista esquerda_1, se a quantidade de elementos for maior que 1, encontre o meio e separe-a em duas listas: esquerda_1_1 e direta_1_1.
#3-Com base na sublista esquerda_1_1, se a quantidade de elementos for maior que 1, encontre o meio e separe-a em duas listas: esquerda_1_2 e direta_1_2.
#4-Repita o processo até encontrar uma lista com tamanho 1.
#5-Chame a etapa de merge.
#6-Repita o processo para todas as sublistas.

#ETAPA DE MERGE:
#1-Dadas duas listas, cada uma das quais contém 1 valor – para ordenar, basta comparar esses valores e fazer a troca, gerando uma sublista com dois valores ordenados.
#2-Dadas duas listas, cada uma das quais contém 2 valores – para ordenar, basta ir escolhendo o menor valor em cada uma e gerar uma sublista com quatro valores ordenados.
#3-Repita o processo de comparação e junção dos valores até chegar à lista original, agora ordenada.

def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)

    
def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    print(sub_lista_ordenada)
    return sub_lista_ordenada


lista = [10, 9, 5, 8, 11, -1, 3]
executar_merge_sort(lista)