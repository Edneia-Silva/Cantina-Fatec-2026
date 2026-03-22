from produto import Produto
from estoque import Estoque

def testar_estoque():
    coxinha = Produto("Coxinha", 2.00, 5.00, "20/03/2026", "25/03/2026", 50)
    suco = Produto("Suco de Laranja", 3.00, 7.00, "21/03/2026", "28/03/2026", 30)

    estoque = Estoque()
    estoque.adicionar_produto(coxinha)
    estoque.adicionar_produto(suco)

    print("Produtos no estoque:")
    estoque.listar_produtos()

    produto_encontrado = estoque.buscar_produto("Coxinha")
    print("Produto encontrado:", produto_encontrado)

if __name__ == "__main__":
    testar_estoque()


from usuario import Aluno
from pagamento import Pagamento

def testar_pagamento():
    aluno = Aluno("Alana", "IA")
    pagamento = Pagamento(aluno, 7.50)

    print(pagamento)

if __name__ == "__main__":
    testar_pagamento()



from usuario import Aluno, Professor

def testar_usuarios():
    aluno = Aluno("Alex", "IA")
    professor = Professor("João")

    print(aluno)       # Deve mostrar: Maria (Aluno)
    print(professor)   # Deve mostrar: João (Professor)

if __name__ == "__main__":
    testar_usuarios()