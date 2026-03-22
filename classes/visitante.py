from classes.pessoa import Pessoa

class Visitante(Pessoa):
    def __init__(self, nome, documento):
        super().__init__(nome, "Visitante")
        self.documento = documento

    def __str__(self):
        return f"Visitante {self.nome} - Documento: {self.documento}"