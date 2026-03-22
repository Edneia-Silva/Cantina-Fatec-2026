from classes.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, "Aluno")
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.curso}"

    def acessar_cantina(self):
        return f"Aluno {self.nome} acessa a cantina com carteirinha."