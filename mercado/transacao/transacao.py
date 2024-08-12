from datetime import datetime

class Transacao:
    def __init__(self, produto, cliente, quantidade, data_compra=None):
        self.produto = produto
        self.cliente = cliente
        self.quantidade = quantidade
        self.data_compra = data_compra if data_compra else datetime.now()

    def concluir(self):
        self.produto.vender(self.quantidade)