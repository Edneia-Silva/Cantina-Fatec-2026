class Servidor:
    def __init__(self, nome, setor):
        self.nome = nome
        self.setor = setor

    def __str__(self):
        return f"Servidor {self.nome} - {self.setor}"
