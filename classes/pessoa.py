class Pessoa:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

    def __str__(self):
        return f"{self.nome} - {self.categoria}"

    def acessar_cantina(self):
        return f"{self.categoria} {self.nome} acessa a cantina."