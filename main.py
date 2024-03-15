from Lojinha.loja import Loja, ClienteEspecial, ClientePadrao, Produto

loja = Loja()

loja.adicionar_cliente_padrao("11111111111", "Livia", "Sydriao", "26 de maio", "10 de março de 2024")
loja.adicionar_cliente_padrao("22222222222", "Ana", "Araujo", "13 de agosto", "23 de março de 2024")
loja.adicionar_cliente_especial("33333333333", "Ryssa", "Esmeraldo", "5 de marco", "1")

loja.adicionar_produto("001", "Gloss 3D", "50.00")
loja.adicionar_produto("002", "Lápis de olho", "20.00")

loja.adicionar_produto_carrinho_cliente("11111111111", "001")
loja.adicionar_produto_carrinho_cliente("33333333333", "001")
loja.adicionar_produto_carrinho_cliente("33333333333", "002")

#loja.exibir_lista_clientes()
#loja.exibir_lista_produtos()
#loja.exibir_carrinho_cliente("11111111111")
#loja.exibir_carrinho_cliente("22222222222")
loja.calcular_total_carrinho_cliente("11111111111")
loja.calcular_total_carrinho_cliente("33333333333")
