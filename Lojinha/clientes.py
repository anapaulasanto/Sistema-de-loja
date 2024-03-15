from abc import ABC, abstractmethod
from datetime import date

class Cliente(ABC):
    def __init__(self, cpf, nome, sobrenome, nascimento):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento
        self.carrinho_compras = []

    @abstractmethod
    def calcular_valor_final_venda(self):
        pass

    def adicionar_produto_carrinho(self,produto):
        self.carrinho_compras.append(produto)

    
class ClientePadrao(Cliente):
    def __init__(self,cpf, nome, sobrenome, nascimento, data_cadastro_loja):
        super().__init__(cpf, nome, sobrenome, nascimento)
        self.data_cadastro_loja = data_cadastro_loja

    def __str__(self):
        return f"\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nCPF: {self.cpf}\nData de nascimento: {self.nascimento}\nData de cadastro da loja: {self.data_cadastro_loja}\n"  #mostrado como retorno na variavel cliente_padrao

    def calcular_valor_final_venda(self):
        total = 0
        for p in self.carrinho_compras:
            total += float(p.preco)
            return total
        
    

class ClienteEspecial(Cliente):
    def __init__(self,cpf, nome, sobrenome, nascimento, nivel_fidelidade):
        super().__init__(cpf, nome, sobrenome, nascimento)
        self.nivel_fidelidade = nivel_fidelidade

    def __str__(self):
        return f"\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nCPF: {self.cpf}\nData de nascimento: {self.nascimento}\nNivel de fidelidade: {self.nivel_fidelidade}\n"

    def calcular_valor_final_venda(self):
        total = 0
        
        for p in self.carrinho_compras:
            total += float(p.preco)

        if self.nivel_fidelidade == '1':   
            return (total) * 0.9
        
        elif self.nivel_fidelidade == '2':
            return  total * 0.8
        
        if self.nivel_fidelidade == '3':
            return  total * 0.7
    

class Produto:
    total_produtos = 0

    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

        Produto.total_produtos += 1

    def __str__(self):
        return f"\nID do produo: {self.id}\nNome do produto: {self.nome}\nPreço: {self.preco}\n"

    @staticmethod
    def obter_total_produtos_cadastrados():
        return Produto.total_produtos 