from classes.pessoa import Pessoa

class Servidor(Pessoa):
    def __init__(self, nome, setor):
        super().__init__(nome, "Servidor")
        self.setor = setor

    def __str__(self):
        return f"Servidor {self.nome} - {self.setor}"
