class Pessoa:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

    def __str__(self):
        return f"{self.nome} - {self.categoria}"