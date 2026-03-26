from datetime import datetime
from classes.pagamento import Pagamento

class Venda:
    def __init__(self, usuario, estoque, nome_produto, quantidade):
        self._usuario = usuario
        self._nome_produto = nome_produto
        self._valor_total = 0  
        self._data_hora = datetime.now()
        self.data_vencimento = datetime.now() 
        
        # 1. Busca o produto na Lista Encadeada 
        produto = estoque.buscar_produto(nome_produto)
        
        # 2. Validação de estoque 
        if produto and produto.quantidade >= quantidade:
            # Baixa o estoque automaticamente usando o @setter
            produto.quantidade -= quantidade
            
            self._valor_total = produto.preco_venda * quantidade
                        
            # 3. Gera o pagamento PIX
            self._pagamento = Pagamento(usuario, self._valor_total)
            print(f"Venda confirmada: {quantidade}x {nome_produto} para {usuario.nome}.")
        else:
            print(f"Erro: Estoque insuficiente para {nome_produto}.")
            self._pagamento = None

    def __str__(self):
        if self._pagamento:
            return f"RECIBO: {self._usuario.nome} | Total: R${self._valor_total:.2f} | Pago via PIX"
        return "Venda não realizada."