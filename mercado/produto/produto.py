from item_transacionavel import ItemTransacionavel

class Produto(ItemTransacionavel):
    def __init__(self, nome, fornecedores, categorias, quantidade_estoque=0):
        self.nome = nome
        self.fornecedores = fornecedores
        self.categorias = categorias
        self.quantidae_estoque = quantidade_estoque

    def vender(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
        else:
            raise Exception('Não temos essa quantidade em estoque')
