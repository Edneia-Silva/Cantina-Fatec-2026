class Aluno:
    def _init_(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def _str_(self):
        return f"{self.nome} ({self.matricula}) - {self.curso}"