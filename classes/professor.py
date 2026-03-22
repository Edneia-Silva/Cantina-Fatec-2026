class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def __str__(self):
        return f"Professor {self.nome} - {self.disciplina}"