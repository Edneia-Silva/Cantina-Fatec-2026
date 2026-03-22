class Usuario:
    def __init__(self, nome, categoria, curso=None):
        self.nome = nome
        self.categoria = categoria  # aluno, professor, servidor, visitante
        self.curso = curso

    def __str__(self):
        return f"{self.nome} ({self.categoria})"