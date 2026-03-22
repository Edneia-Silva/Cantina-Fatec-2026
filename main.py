from classes.aluno import Aluno
from classes.professor import Professor
from classes.servidor import Servidor
from classes.visitante import Visitante

aluno1 = Aluno("Roger", "123", "IA")
aluno2 = Aluno("Brianna", "456", "ESG")
professor1 = Professor("Orlando", "Estrutura de Dados")
servidor1 = Servidor("Carlos", "Biblioteca")
visitante1 = Visitante("Fernanda", "RG 987654")

usuarios = [aluno1, aluno2, professor1, servidor1, visitante1]

for usuario in usuarios:
    print(usuario)
    print(usuario.acessar_cantina())
    print("-" * 40)

    from classes.produto import Produto

# Criando produtos
produto1 = Produto("Coxinha", 3.00, 5.00, "20/03/2026", "25/03/2026", 10)
produto2 = Produto("Suco", 2.00, 4.00, "19/03/2026", "30/03/2026", 5)

# Testando estoque
print(produto1)
produto1.baixar_estoque(2)
print("Depois da venda:", produto1)