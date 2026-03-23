from classes.usuario import Aluno, Professor
from classes.produto import Produto
from classes.estoque import Estoque
from classes.venda import Venda
from classes.pagamento import Pagamento

def testar_venda_suco_antigo_primeiro():
    aluno = Aluno("Alana", "IA")

    suco_antigo = Produto("Suco de Laranja", 3.00, 7.00, "15/03/2026", "25/03/2026", 5)
    suco_novo   = Produto("Suco de Laranja", 3.00, 7.00, "20/03/2026", "30/03/2026", 10)

    estoque = Estoque()
    estoque.adicionar_produto(suco_antigo)
    estoque.adicionar_produto(suco_novo)

    print("\n--- Estoque antes da venda ---")
    estoque.listar_produtos()

    venda = Venda(aluno, estoque, "Suco de Laranja", 7)
    print(venda)
    print("Pagamento:", venda.pagamento)

    print("\n--- Estoque após a venda ---")
    estoque.listar_produtos()


def testar_venda_coxinha_antigo_primeiro():
    aluno = Aluno("Alana", "IA")

    coxinha_antiga = Produto("Coxinha", 2.00, 5.00, "15/03/2026", "25/03/2026", 5)
    coxinha_nova   = Produto("Coxinha", 2.00, 5.00, "20/03/2026", "30/03/2026", 10)

    estoque = Estoque()
    estoque.adicionar_produto(coxinha_antiga)
    estoque.adicionar_produto(coxinha_nova)

    print("\n--- Estoque antes da venda ---")
    estoque.listar_produtos()

    venda = Venda(aluno, estoque, "Coxinha", 7)
    print(venda)
    print("Pagamento:", venda.pagamento)

    print("\n--- Estoque após a venda ---")
    estoque.listar_produtos()


def testar_edicao_quantidade():
    estoque = Estoque()
    estoque.adicionar_produto(Produto("Pastel", 4.00, 6.00, "20/03/2026", "25/03/2026", 10))

    print("\n--- Estoque inicial ---")
    estoque.listar_produtos()

    print("\n--- Editando quantidade ---")
    print(estoque.editar_quantidade("Pastel", 15))   # Atualiza quantidade
    print(estoque.editar_quantidade("Suco", 5))      # Produto inexistente

    print("\n--- Estoque após edição ---")
    estoque.listar_produtos()


if __name__ == "__main__":
    testar_venda_suco_antigo_primeiro()
    testar_venda_coxinha_antigo_primeiro()
    testar_edicao_quantidade()