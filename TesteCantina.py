from classes.usuario import Usuario
from classes.produto import Produto
from classes.estoque import Estoque
from classes.venda import Venda
from faker import Faker

def testar_venda_fifo():
    # Commit 17
    aluno = Usuario("Alana", "Aluno", "IA")
    estoque = Estoque()
    estoque.adicionar_produto(Produto("Suco de Laranja", 5, 7, "20/03/2026", "25/03/2026", 5))
    estoque.adicionar_produto(Produto("Suco de Laranja", 5, 7, "20/03/2026", "30/03/2026", 10))

    print("\n--- Estoque antes da venda ---")
    estoque.listar_produtos()

    # Primeira venda: 5 unidades do primeiro lote
    venda1 = Venda(aluno, estoque, "Suco de Laranja", 5)
    print(venda1)

    # Segunda venda: 2 unidades do segundo lote
    venda2 = Venda(aluno, estoque, "Suco de Laranja", 2)
    print(venda2)

    print("\n--- Estoque após a venda ---")
    estoque.listar_produtos()

def testar_edicao_estoque():
    # Commit 18
    estoque = Estoque()
    estoque.adicionar_produto(Produto("Pastel", 4, 6, "20/03/2026", "25/03/2026", 10))

    print("\n--- Estoque inicial ---")
    estoque.listar_produtos()

    print("\n--- Editando quantidade ---")
    estoque.editar_quantidade("Pastel", 15)
    estoque.editar_quantidade("Suco", 20)

    print("\n--- Estoque após edição ---")
    estoque.listar_produtos()

def testar_faker_cantina():
    # Commit 19
    faker = Faker("pt_BR")
    estoque = Estoque()

    # Criar produtos aleatórios
    for _ in range(3):
        nome_produto = faker.word().capitalize()
        preco_custo = round(faker.random_number(digits=2) / 2, 2)
        preco_venda = preco_custo + round(faker.random_number(digits=1), 2)
        validade = faker.date_between(start_date="today", end_date="+30d").strftime("%d/%m/%Y")
        quantidade = faker.random_int(min=5, max=20)

        produto = Produto(nome_produto, preco_custo, preco_venda, "20/03/2026", validade, quantidade)
        estoque.adicionar_produto(produto)

    print("\n--- Estoque gerado com Faker ---")
    estoque.listar_produtos()

    # Criar aluno aleatório
    aluno = Usuario(faker.first_name(), "Aluno", "IA")

    # Criar venda aleatória
    produto_escolhido = estoque.produtos[0]
    quantidade_venda = faker.random_int(min=1, max=produto_escolhido.quantidade)

    venda = Venda(aluno, estoque, produto_escolhido.nome, quantidade_venda)
    print(venda)

    print("\n--- Estoque após venda aleatória ---")
    estoque.listar_produtos()

# Chamadas de teste
testar_venda_fifo()
testar_edicao_estoque()
testar_faker_cantina()

