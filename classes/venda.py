from datetime import datetime
from pagamento import Pagamento

class Venda:
    def __init__(self, usuario, estoque, nome_produto, quantidade):
        self.usuario = usuario
        self.data_hora = datetime.now()
        self.quantidade = quantidade

        # Consome do estoque (mais antigos primeiro)
        vendidos = estoque.vender_produto(nome_produto, quantidade)
        if not vendidos:
            raise ValueError("Estoque insuficiente ou produto vencido.")

        self.itens = vendidos
        self.valor_total = sum(produto.preco_venda * qtd for produto, qtd in vendidos)
        self.pagamento = Pagamento(usuario, self.valor_total)
    
    def __str__(self):
        itens_str = ", ".join([f"{qtd}x {produto.nome}" for produto, qtd in self.itens])
        return (f"Venda realizada: {self.usuario.nome} comprou {itens_str} "
            f"por R${self.valor_total:.2f} em {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"{self.pagamento}")