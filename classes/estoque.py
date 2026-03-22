class Estoque:
    def __init__(self):
        # Lista que vai armazenar os produtos
        self.produtos = []

    def adicionar_produto(self, produto):
        # Adiciona um novo produto ao estoque
        self.produtos.append(produto)

    def listar_produtos(self):
        # Mostra todos os produtos cadastrados
        for p in self.produtos:
            print(p)

    def buscar_produto(self, nome):
        # Procura um produto pelo nome
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                return p
        return None