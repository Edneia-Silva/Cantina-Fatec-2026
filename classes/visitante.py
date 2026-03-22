class Visitante:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f"Visitante {self.nome} - Documento: {self.documento}"