class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""

    def __init__(self): 
        self.cabeca = None


    def __repr__(self):
        return "[" + str(self.cabeca) + "]"


    def insere_no_inicio(self, novo_dado):
        """Insere um elemento no começo da lista."""
        
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)
        
        # Faz com que o novo nodo seja a cabeça da lista.
        novo_nodo.proximo = self.cabeca
        
        # Faz com que a cabeça da lista referencie o novo nodo.
        self.cabeca = novo_nodo


    def insere_depois(self, nodo_anterior, novo_dado):
        """Insere um elemento após outro elemento na lista."""
        
        assert nodo_anterior, "Nodo anterior precisa existir na lista."
        
        # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)
        
        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.proximo
        
        # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.proximo = novo_nodo

    
    def remove(self, valor):
        """Remove um elemento da lista."""
        
        assert self.cabeca, "Impossível remover valor de lista vazia."
        
        # Nodo a ser removido é a cabeça da lista.
        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            # Encontra a posição do elemento a ser removido.
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo            
            
            # O nodo corrente é o nodo a ser removido.
            if corrente:                
                anterior.proximo = corrente.proximo
            else:
                # O nodo corrente é a cauda da lista.
                anterior.proximo = None

                
    def busca(self, valor):
        """Procura por um elemento na lista."""

        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente