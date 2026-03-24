from usuario import Aluno, Professor
from produto import Produto
from estoque import Estoque
from venda import Venda
from pagamento import Pagamento

def testar_venda_suco_antigo_primeiro():
    aluno = Aluno("Alana", "IA")

    suco_antigo = Produto("Suco de Laranja", 3.00, 7.00, "15/03/2026", "25/03/2026", 5)
    suco_novo   = Produto("Suco de Laranja", 3.00, 7.00, "20/03/2026", "30/03/2026", 10)

    estoque = Estoque()
    estoque.adicionar_produto(suco_antigo)
    estoque.adicionar_produto(suco_novo)

    print("Estoque antes da venda:")
    estoque.listar_produtos()

    venda = Venda(aluno, estoque, "Suco de Laranja", 7)
    print(venda)
    print("Pagamento:", venda.pagamento)

    print("\nEstoque após a venda:")
    estoque.listar_produtos()


def testar_venda_coxinha_antigo_primeiro():
    aluno = Aluno("Alana", "IA")

    coxinha_antiga = Produto("Coxinha", 2.00, 5.00, "15/03/2026", "25/03/2026", 5)
    coxinha_nova   = Produto("Coxinha", 2.00, 5.00, "20/03/2026", "30/03/2026", 10)

    estoque = Estoque()
    estoque.adicionar_produto(coxinha_antiga)
    estoque.adicionar_produto(coxinha_nova)

    print("Estoque antes da venda:")
    estoque.listar_produtos()

    venda = Venda(aluno, estoque, "Coxinha", 7)
    print(venda)
    print("Pagamento:", venda.pagamento)

    print("\nEstoque após a venda:")
    estoque.listar_produtos()


if __name__ == "__main__":
    testar_venda_suco_antigo_primeiro()
    # testar_venda_coxinha_antigo_primeiro()


