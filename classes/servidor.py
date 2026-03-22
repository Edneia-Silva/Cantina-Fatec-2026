class Servidor:
    def _init_(self, nome, setor):
        self.nome = nome
        self.setor = setor

    def _str_(self):
        return f"Servidor {self.nome} - {self.setor}"
