#complexidade O(N2) - algoritmos lentos, mas fáceis de entender
    #selection sort
    #bubble sort
    #insertion sort
    
#complexidade O(N log N) - algoritmos com performance superior, mas mais complexo de entender
    #merge sort
    #quick sort
    
#BUBBLE SORT
#Iteração 1: seleciona o valor na posição 0 e o compara com 
    # seu vizinho – se for menor, há troca; se não for, seleciona 
    # o próximo e compara, repentindo o processo.
#Iteração 2: seleciona o valor na posição 0 e compara ele com 
    # seu vizinho, se for menor troca, senão seleciona o próximo e 
    # compara, repentindo o processo.
#Iteração N - 1: seleciona o valor na posição 0 e o compara 
    # com seu vizinho – se for menor, há troca; se não for, 
    # seleciona o próximo e compara, repentindo o processo.
    
def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
executar_bubble_sort(lista)

print(lista)