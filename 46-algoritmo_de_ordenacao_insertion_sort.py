#complexidade O(N2) - algoritmos lentos, mas fáceis de entender
    #selection sort
    #bubble sort
    #insertion sort
    
#complexidade O(N log N) - algoritmos com performance superior, mas mais complexo de entender
    #merge sort
    #quick sort
    
#INSERTION SORT
#Início: parte-se do princípio de que a lista possui um único valor e, consequentemente, está ordenada.
#Iteração 1: parte-se do princípio de que um novo valor precisa ser inserido na lista; nesse caso, ele é comparado com o valor já existente para saber se precisa ser feita uma troca de posição.
#Iteração 2: parte-se do princípio de que um novo valor precisa ser inserido na lista; nesse caso, ele é comparado com os valores já existentes para saber se precisam ser feitas trocas de posição.
#Iteração N: parte-se do princípio de que um novo valor precisa ser inserido na lista; nesse caso, ele é comparado com todos os valores já existentes (desde o início) para saber se precisam ser feitas trocas de posição.

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i] 
        j = i - 1
        
        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir
    
    return lista


lista = [10, 9, 5, 8, 11, -1, 3]
executar_insertion_sort(lista)

print(lista)