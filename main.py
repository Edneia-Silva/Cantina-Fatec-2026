import pickle
from faker import Faker
from classes.estoque import Estoque
from classes.produto import Produto
from classes.aluno import Aluno
from classes.visitante import Visitante
from classes.venda import Venda
from classes.relatorio import Relatorio
from classes.estrutura_dados import ListaEncadeada

fake = Faker('pt_BR')

def salvar_dados(estoque):
    with open('estoque_cantina.pkl', 'wb') as f:
        pickle.dump(estoque, f)
    print("\n[Sistema] Dados salvos com sucesso!")

def carregar_dados():
    try:
        with open('estoque_cantina.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Estoque()

def executar_sistema():
    estoque = carregar_dados()
    lista_de_vendas = ListaEncadeada()
    
    # Gera dados fictícios com Faker 
    if not estoque.buscar_produto("Coxinha"):
        if not estoque.buscar_produto("Coxinha"):
            print("[Sistema] Gerando estoque inicial variado...")
        
        # 1. SALGADOS
        p1 = Produto("Coxinha", 4.0, 8.0, "26/03/2026", "28/03/2026", 100)
        p3 = Produto("Pão de Queijo", 2.5, 5.0, "26/03/2026", "27/03/2026", 50)
        p4 = Produto("Enroladinho", 3.5, 7.5, "26/03/2026", "29/03/2026", 40)
        p6 = Produto("Kibe Assado", 4.5, 9.0, "26/03/2026", "27/03/2026", 50)
        
        # 2. BEBIDAS
        p2 = Produto("Suco Natural", 3.0, 6.0, "26/03/2026", "27/03/2026", 30)
        p5 = Produto("Café Expresso", 2.0, 4.5, "26/03/2026", "30/12/2026", 100)
        p10 = Produto("Refrigerante Lata", 3.5, 7.0, "26/03/2026", "20/12/2026", 60)

        # --- 3 NOVOS DOCES ---
        p7 = Produto("Brigadeiro Gourmet", 2.0, 5.0, "26/03/2026", "30/03/2026", 40)
        p8 = Produto("Bolo de Pote", 5.0, 12.0, "26/03/2026", "29/03/2026", 20)
        p9 = Produto("Paçoca", 0.5, 1.5, "26/03/2026", "30/06/2027", 100)

        # 3. CADASTRAR TODOS NA LISTA ENCADEADA
        estoque.cadastrar(p1)
        estoque.cadastrar(p2)
        estoque.cadastrar(p3)
        estoque.cadastrar(p4)
        estoque.cadastrar(p5)
        estoque.cadastrar(p6)
        estoque.cadastrar(p7)
        estoque.cadastrar(p8)
        estoque.cadastrar(p9)
        estoque.cadastrar(p10)

    # Cria usuários 
    aluno = Aluno(fake.name(), "Inteligência Artificial")
    visitante = Visitante(fake.name(), fake.rg())
    
    print(f"\n--- Simulação de Acesso ---")
    print(aluno.acessar_cantina())
    print(visitante.acessar_cantina())

    print("\n--- Processando Fluxo de Vendas (10 Transações) ---")

    # Bloco de Salgados
    v1 = Venda(aluno, estoque, "Coxinha", 2)
    lista_de_vendas.adicionar_por_vencimento(v1)
    
    v2 = Venda(visitante, estoque, "Pão de Queijo", 3)
    lista_de_vendas.adicionar_por_vencimento(v2)
    
    v3 = Venda(aluno, estoque, "Kibe Assado", 1)
    lista_de_vendas.adicionar_por_vencimento(v3)

    # Bloco de Bebidas
    v4 = Venda(aluno, estoque, "Suco Natural", 1)
    lista_de_vendas.adicionar_por_vencimento(v4)
    
    v5 = Venda(visitante, estoque, "Refrigerante Lata", 2)
    lista_de_vendas.adicionar_por_vencimento(v5)
    
    v6 = Venda(aluno, estoque, "Café Expresso", 1)
    lista_de_vendas.adicionar_por_vencimento(v6)

    # Bloco de Doces
    v7 = Venda(visitante, estoque, "Bolo de Pote", 1)
    lista_de_vendas.adicionar_por_vencimento(v7)
    
    v8 = Venda(aluno, estoque, "Brigadeiro Gourmet", 4)
    lista_de_vendas.adicionar_por_vencimento(v8)
    
    v9 = Venda(visitante, estoque, "Paçoca", 10)
    lista_de_vendas.adicionar_por_vencimento(v9)

    # A "Venda Extra" para fechar os 10
    v10 = Venda(aluno, estoque, "Enroladinho", 1)
    lista_de_vendas.adicionar_por_vencimento(v10)

    # Lista estoque atualizado
    estoque.listar_produtos()

    # Salva tudo (Persistência)
    salvar_dados(estoque)

    print("\n--- Gerando Relatórios Finais ---")
    relat = Relatorio(lista_de_vendas)
    relat.gerar_vendas_financeiro()
    relat.gerar_consumo_perfil()

if __name__ == "__main__":
    executar_sistema()