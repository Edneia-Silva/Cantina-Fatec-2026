from faker import Faker
import pickle

from classes.usuario import Usuario
from classes.produto import Produto
from classes.estoque import Estoque
from classes.venda import Venda

# Funções de relatório
def relatorio_vendas(vendas):
    print("\n--- Relatório de Vendas ---")
    for venda in vendas:
        print(venda)

def relatorio_consumo(estoque_inicial, estoque_final):
    print("\n--- Relatório de Consumo ---")
    nomes_finais = [p.nome for p in estoque_final.produtos]
    for produto_inicial in estoque_inicial.produtos:
        if produto_inicial.nome in nomes_finais:
            produto_final = next(p for p in estoque_final.produtos if p.nome == produto_inicial.nome)
            consumido = produto_inicial.quantidade - produto_final.quantidade
        else:
            consumido = produto_inicial.quantidade  # produto foi totalmente consumido
        print(f"{produto_inicial.nome}: {consumido} unidades consumidas")

def testar_faker_cantina():
    faker = Faker("pt_BR")
    estoque = Estoque()

    # Guardar estoque inicial para relatório de consumo
    estoque_inicial = Estoque()

    # Criar produtos aleatórios
    for _ in range(3):
        nome_produto = faker.word().capitalize()
        preco_custo = round(faker.random_number(digits=2) / 2, 2)
        preco_venda = preco_custo + round(faker.random_number(digits=1), 2)
        validade = faker.date_between(start_date="today", end_date="+30d").strftime("%d/%m/%Y")
        quantidade = faker.random_int(min=5, max=20)

        produto = Produto(nome_produto, preco_custo, preco_venda, "20/03/2026", validade, quantidade)
        estoque.adicionar_produto(produto)
        estoque_inicial.adicionar_produto(Produto(nome_produto, preco_custo, preco_venda, "20/03/2026", validade, quantidade))

    print("\n--- Estoque gerado com Faker ---")
    estoque.listar_produtos()

    # Criar aluno e venda aleatória
    aluno = Usuario(faker.first_name(), "Aluno", "IA")
    produto_escolhido = estoque.produtos[0]
    quantidade_venda = faker.random_int(min=1, max=produto_escolhido.quantidade)

    venda = Venda(aluno, estoque, produto_escolhido.nome, quantidade_venda)
    print(venda)

    print("\n--- Estoque após venda aleatória ---")
    estoque.listar_produtos()

    # 🔹 Salvar com pickle
    with open("estoque.pkl", "wb") as f:
        pickle.dump(estoque, f)
    with open("vendas.pkl", "wb") as f:
        pickle.dump([venda], f)

    print("\nDados salvos em estoque.pkl e vendas.pkl")

    # Relatórios
    relatorio_vendas([venda])
    relatorio_consumo(estoque_inicial, estoque)

def carregar_dados():
    with open("estoque.pkl", "rb") as f:
        estoque_carregado = pickle.load(f)
    with open("vendas.pkl", "rb") as f:
        vendas_carregadas = pickle.load(f)

    print("\n--- Estoque carregado do arquivo ---")
    estoque_carregado.listar_produtos()

    relatorio_vendas(vendas_carregadas)

# Chamadas de teste
testar_faker_cantina()
carregar_dados()