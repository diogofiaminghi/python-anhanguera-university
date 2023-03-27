

lista = [10, 4, 1, 15, -3]

print('lista = ', lista, '\n')

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print('lista_ordenada1 = ', lista_ordenada1)
print('lista_ordenada2 = ', lista_ordenada2)
print('lista = ', lista)

#Logo, concluímos que: 
# 1) a função built-in sorted() não altera a lista original e 
# faz a ordenação em uma nova lista; e 
# 2) o método sort() faz a ordenação na lista original com 
# retorno None.