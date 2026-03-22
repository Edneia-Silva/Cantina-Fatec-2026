from classes.aluno import Aluno
from classes.professor import Professor
from classes.servidor import Servidor
from classes.visitante import Visitante

aluno1 = Aluno("Roger", "123", "IA")
aluno2 = Aluno("Brianna", "456", "ESG")
professor1 = Professor("Orlando", "Estrutura de Dados")
servidor1 = Servidor("Carlos", "Biblioteca")
visitante1 = Visitante("Fernanda", "RG 987654")

pessoas = [aluno1, aluno2, professor1, servidor1, visitante1]

for pessoa in pessoas:
    print(pessoa)
    print(pessoa.acessar_cantina())
    print("-" * 40)