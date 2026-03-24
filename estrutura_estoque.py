class EstruturaEstoque:
    def __init__(self):
        self._dados = []

    def adicionar(self, produto):
        self._dados.append(produto)

    def listar(self):
        return self._dados

    def ordenar_por_data(self):
        self._dados.sort(key=lambda p: p.data_compra)

    def remover_zerados(self):
        self._dados = [p for p in self._dados if p.quantidade > 0]