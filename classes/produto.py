from datetime import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self._nome = nome
        self._preco_compra = preco_compra
        self._preco_venda = preco_venda
        # Importante: converter para data para a Lista Encadeada comparar depois
        self._data_compra = datetime.strptime(data_compra, "%d/%m/%Y")
        self._data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self._quantidade = quantidade

    @property
    def nome(self): return self._nome

    @property
    def preco_venda(self): return self._preco_venda

    @property
    def data_vencimento(self): return self._data_vencimento

    @property
    def quantidade(self): return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor >= 0:
            self._quantidade = valor
        else:
            print("Erro: Quantidade inválida!")