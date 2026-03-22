from classes.usuario import Usuario

class Visitante(Usuario):
    def __init__(self, nome, documento):
        super().__init__(nome, "Visitante")
        self.documento = documento

    def __str__(self):
        return f"Visitante {self.nome} - Documento: {self.documento}"

    def acessar_cantina(self):
        return f"Visitante {self.nome} acessa a cantina com documento e autorização."