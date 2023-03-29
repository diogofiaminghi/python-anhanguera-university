
#VEJA QUE TANTO A CLASSE FUNCIONARIO COMO A CLASSE CLIENTE
#HERDAM A CLASSE PESSOA

class Pessoa:
    
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    
    def __init__(self):
        self.matricula = None
        self.salacio = None
    
    def bater_ponto(self):
        # código aqui
        pass
    
    def fazer_login(self):
        # código aqui
        pass

class Cliente(Pessoa):
    
    def __init__(self):
        self.codigo = None
        self.dataCadastro = None
    
    def fazer_compra(self):
        # código aqui
        pass
    
    def pagar_conta(self):
        # código aqui
        pass

f1 = Funcionario()
f1.nome = "Funcionário A"
print(f1.nome)

c1 = Cliente()
c1.cpf = "111.111.111-11"
print(c1.cpf)

#METODOS MAGICOS EM PYTHON - Quando uma classe é criada 
#em Python, ela herda, mesmo que não declarado 
#explicitamente, todos os recursos de uma classe-base 
#chamada object.

print(dir(Pessoa()))