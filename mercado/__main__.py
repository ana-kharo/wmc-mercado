from mercado.mercado import Mercado
from mercado.cliente import Cliente
from mercado.fornecedor import Produto
from mercado.produto import Fornecedor
from mercado.transacao import Transacao

# Exemplo de transação no mercado
if __name__ == "__main__":
    mercado = Mercado()

    cliente = Cliente("Ana Kharo", "123456789", "Rua Pedro Pires, 123")
    mercado.adicionar_cliente(cliente)

    fornecedor = Fornecedor("Fornecedor 1")
    produto = Produto("Arroz", [fornecedor], ["Alimentos"], 25)
    mercado.adicionar_produto(produto)

    transacao = Transacao(produto, cliente, 2)
    mercado.registrar_transacao(transacao)