class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.curso}"