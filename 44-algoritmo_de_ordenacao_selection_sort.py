#complexidade O(N2) - algoritmos lentos, mas fáceis de entender
    #selection sort
    #bubble sort
    #insertion sort
    
#complexidade O(N log N) - algoritmos com performance superior, mas mais complexo de entender
    #merge sort
    #quick sort
    
#SELECTION SORT
#Iteração 1: percorre toda a lista, procurando o menor valor para ocupar a posição 0.
#Iteração 2: a partir da posição 1, percorre toda a lista, procurando o menor valor para ocupar a posição 1.
#Iteração 3: a partir da posição 2, percorre toda a lista, procurando o menor valor para ocupar a posição 2.
#Esse processo é repetido N-1 vezes, sendo N o tamanho da lista.

def executar_selection_sort(lista):
    n = len(lista)
    
    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista


lista = [10, 9, 5, 8, 11, -1, 3]
executar_selection_sort(lista)

print(lista)