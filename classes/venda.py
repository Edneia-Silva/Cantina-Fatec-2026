from datetime import datetime
from pagamento import Pagamento

class Venda:
    def __init__(self, usuario, produto, quantidade):
        self.usuario = usuario
        self.produto = produto
        self.quantidade = quantidade
        self.data_hora = datetime.now()
        self.valor_total = produto.preco_venda * quantidade
        self.pagamento = Pagamento(usuario, self.valor_total)

    def __str__(self):
        return (f"Venda realizada: {self.usuario.nome} comprou {self.quantidade}x {self.produto.nome} "
                f"por R${self.valor_total:.2f} em {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}")