from classes.usuario import Usuario

class Servidor(Usuario):
    def __init__(self, nome, setor):
        super().__init__(nome, "Servidor")
        self.setor = setor

    def __str__(self):
        return f"Servidor {self.nome} - {self.setor}"

    def acessar_cantina(self):
        return f"Servidor {self.nome} acessa a cantina com crachá funcional."
