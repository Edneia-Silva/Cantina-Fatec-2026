from datetime import datetime

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            for produto in self.produtos:
                print(f"{produto.nome} | Estoque: {produto.quantidade} | Preço venda: R${produto.preco_venda}")

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def vender_produto(self, nome, quantidade):
        vendidos = []
        restante = quantidade
        hoje = datetime.now().date()

        # Ordena pela data de entrada (mais antigos primeiro)
        self.produtos.sort(key=lambda p: p.data_compra.date())

        for produto in self.produtos:
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

        self.produtos = [p for p in self.produtos if p.quantidade > 0]

        return vendidos if restante == 0 else None