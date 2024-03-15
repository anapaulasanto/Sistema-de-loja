from Lojinha.clientes import ClientePadrao, ClienteEspecial, Produto
    
class Loja:
    def __init__(self):
        self.lista_clientes = []  #lista com meus clientes da loja, recebe cliente_padrao que contem o retorno da classe ClientePadrao com os dados no str
        self.lista_produtos = []  #lista com meus produtos da loja


    def exibir_lista_clientes(self):
        print('\n---------- LISTA DE CLIENTES ------------')
        if self.lista_clientes:
            for indice, dado in enumerate(self.lista_clientes, start=1):
                print(f'\t\tCliente: {indice}: {dado}')



    def exibir_lista_produtos(self):
        print('\n---------- LISTA DE PRODUTOS ------------')
        if self.lista_produtos:
            for indice, dado in enumerate(self.lista_produtos, start=1):
                print(f'\t\tProduto: {indice}: {dado}')


    def exibir_carrinho_cliente(self,cpf):
        print('\n---------- CARRINHO ------------')
        cliente = self.obter_cliente_por_cpf(cpf)    #utilizo o self.obter_cliente_por_cpf pq ele esta instanciado nessa classe. Estou chamando o metodo obter_cliente que pertence a classe loja(self), a classe q estamos, ele vai passar o cliente do cpf fornecido que ta na lista de clientes e armazenar na variavel cliente

        if cliente:
            print(f'\tCarrinho de compras do cliente {cliente.nome}:')
            if cliente.carrinho_compras:  #se o carrinho do cliente existir (usa cliente. pq carrinho de compras n esta na mesma classe)
                for p in cliente.carrinho_compras:  #para p, (que cada p é uma instancia de Produto, contendo id, nome e preco, que sao os atributos da classe) que percorre o carrinho_compras de um cliente especifico
                    print(f'\t{p.nome} - {p.preco}') #printo cada p
            else:
                print("\tCarrinho de compras está vazio!")



    def adicionar_cliente_padrao(self, cpf, nome, sobrenome, nascimento, data_cadastro_loja):
        cliente_padrao = ClientePadrao(cpf, nome,sobrenome,nascimento,data_cadastro_loja) #cliente_padrao recebe o retorno da minha classe, a classe retorna o str
        self.lista_clientes.append(cliente_padrao)
        print(f'\nCliente {nome} adicionado com sucesso!')



    def adicionar_cliente_especial(self, cpf, nome, sobrenome, nascimento, nivel_fidelidade):
        cliente_especial = ClienteEspecial(cpf, nome, sobrenome, nascimento, nivel_fidelidade)
        self.lista_clientes.append(cliente_especial)
        print(f'\nCliente {nome} adicionado com sucesso!')



    def adicionar_produto(self,  id, nome, preco):
       produto = Produto(id,nome,preco)
       self.lista_produtos.append(produto)
       print(f'\n{nome} adicionado com sucesso!')



    def adicionar_produto_carrinho_cliente(self, cpf, id):
        cliente = self.obter_cliente_por_cpf(cpf)
        produto = self.obter_produto_por_id(id)

        if cliente and produto:
            if isinstance(cliente, ClientePadrao):          
                cliente.adicionar_produto_carrinho(produto) #adiciona o produto no carrinho do cliente especifico, por isso cliente.adicionar_produto.. pq esse metodo nao pertence a classe loja
                print('\nProduto adicionado ao carrinho do Cliente Padrão!')
            elif isinstance(cliente, ClienteEspecial):
                cliente.adicionar_produto_carrinho(produto)
                print('\nProduto adicionado ao carrinho do Cliente Especial!')
        else:
            print('\tCliente ou produto não encontrado!')


    
    def calcular_total_carrinho_cliente(self, cpf):
        cliente = self.obter_cliente_por_cpf(cpf)

        if isinstance(cliente, ClientePadrao):
            total = cliente.calcular_valor_final_venda()
            print(f'\nValor total do carrinho de {cliente.nome}: R${total}')

        elif isinstance(cliente, ClienteEspecial):
            total = cliente.calcular_valor_final_venda()
            print(f'\nValor total do carrinho de {cliente.nome}: R${total}')


    
    def obter_cliente_por_cpf(self,cpf):
        for c in self.lista_clientes:
            if c.cpf == cpf:
                return c
        return None
    
    
    def obter_produto_por_id(self,id):
        for p in self.lista_produtos:
            if p.id == id:
                return p
        return None
        

                
            
        