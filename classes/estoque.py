from classes.estrutura_dados import ListaEncadeada

class Estoque:
    def __init__(self):          
        self._lista = ListaEncadeada() 

    def cadastrar(self, produto):      
        self._lista.adicionar_por_vencimento(produto)

    def listar_produtos(self):              
        atual = self._lista.cabeca
        if atual is None:
            print("Estoque vazio.")
            return

        print("\n--- Itens em Estoque (Ordenados por Vencimento) ---")
        while atual is not None:
            p = atual.produto
            print(f"Produto: {p.nome} | Qtd: {p.quantidade} | Vence: {p.data_vencimento.strftime('%d/%m/%Y')}")
            atual = atual.proximo

    def buscar_produto(self, nome):
        atual = self._lista.cabeca
        while atual is not None:
            if atual.produto.nome.lower() == nome.lower():
                return atual.produto
            atual = atual.proximo
        return None