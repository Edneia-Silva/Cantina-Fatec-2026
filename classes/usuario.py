class Usuario:
    def __init__(self, nome, categoria, curso=None):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso

    def __str__(self):
        return f"{self.nome} ({self.categoria})"

class Aluno(Usuario):
    def __init__(self, nome, curso):
        super().__init__(nome, "Aluno", curso)

class Professor(Usuario):
    def __init__(self, nome):
        super().__init__(nome, "Professor")

class Servidor(Usuario):
    def __init__(self, nome):
        super().__init__(nome, "Servidor")

class Visitante(Usuario):
    def __init__(self, nome):
        super().__init__(nome, "Visitante")