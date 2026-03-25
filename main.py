import pickle
from faker import Faker
from classes.estoque import Estoque
from classes.produto import Produto
from classes.aluno import Aluno
from classes.visitante import Visitante
from classes.venda import Venda

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
    # Carrega ou inicializa o Estoque 
    estoque = carregar_dados()
    
    # Gera dados fictícios com Faker 
    if not estoque.buscar_produto("Coxinha"):
        print("[Sistema] Gerando estoque inicial...")
        p1 = Produto("Coxinha", 4.0, 8.0, "20/03/2026", "28/03/2026", 50)
        p2 = Produto("Suco Natural", 3.0, 6.0, "20/03/2026", "25/03/2026", 30)
        estoque.cadastrar(p1)
        estoque.cadastrar(p2)

    # Cria usuários 
    aluno = Aluno(fake.name(), "Inteligência Artificial")
    visitante = Visitante(fake.name(), fake.rg())
    
    print(f"\n--- Simulação de Acesso (Polimorfismo) ---")
    print(aluno.acessar_cantina())
    print(visitante.acessar_cantina())

    # Realizar uma venda 
    print("\n--- Realizando Venda ---")
    venda1 = Venda(aluno, estoque, "Coxinha", 2)
    print(venda1)

    # Lista estoque atualizado
    estoque.listar_produtos()

    # Salvar tudo (Persistência)
    salvar_dados(estoque)

if __name__ == "__main__":
    executar_sistema()