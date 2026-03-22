from datetime import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = datetime.strptime(data_compra, "%d/%m/%Y")
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self.quantidade = quantidade

    def baixar_estoque(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            return True
        return False

    def __str__(self):
        return f"{self.nome} | Estoque: {self.quantidade} | Preço venda: R${self.preco_venda}"