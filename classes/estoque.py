from datetime import datetime
from estrutura_estoque import EstruturaEstoque

class Estoque:
    def __init__(self):
        self.produtos = EstruturaEstoque()

    def adicionar_produto(self, produto):
        self.produtos.adicionar(produto)

    def listar_produtos(self):
        if not self.produtos.listar():
            print("Estoque vazio.")
        else:        
            for produto in self.produtos.listar():
                print(f"{produto.nome} | Estoque: {produto.quantidade} | Preço venda: R${produto.preco_venda}")

    def buscar_produto(self, nome):
        for produto in self.produtos.listar():
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def vender_produto(self, nome, quantidade):
        vendidos = []
        restante = quantidade
        hoje = datetime.now().date()

        # Ordena pela data de entrada (mais antigos primeiro)
        self.produtos.ordenar_por_data()

        for produto in self.produtos.listar():
            data_venc = produto.data_vencimento.date()
            if data_venc < hoje:
                print(f"Produto vencido removido: {produto.nome}")
                produto.quantidade = 0
                continue

            if produto.nome.lower() == nome.lower() and restante > 0:
                if produto.quantidade >= restante:
                    produto.quantidade -= restante
                    vendidos.append((produto, restante))
                    restante = 0
                else:
                    vendidos.append((produto, produto.quantidade))
                    restante -= produto.quantidade
                    produto.quantidade = 0

        self.produtos.remover_zerados()

        return vendidos if restante == 0 else None
    
    # Novo método para editar quantidade
    def editar_quantidade(self, nome, nova_quantidade):
        produto = self.buscar_produto(nome)
        if produto:
            produto.quantidade = nova_quantidade
            return f"Quantidade do produto {nome} atualizada para {nova_quantidade}."
        else:
            return f"Produto {nome} não encontrado no estoque."
