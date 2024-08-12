class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f'Cliente: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereco}'