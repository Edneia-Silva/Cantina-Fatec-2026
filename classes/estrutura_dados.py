class No:
    def __init__(self, produto):
        self.produto = produto  
        self.proximo = None     

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  

    def adicionar_por_vencimento(self, novo_produto):
        novo_no = No(novo_produto)               
       
        if self.cabeca is None or novo_produto.data_vencimento < self.cabeca.produto.data_vencimento:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return
        
        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.produto.data_vencimento < novo_produto.data_vencimento:
            atual = atual.proximo
        
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
    
    