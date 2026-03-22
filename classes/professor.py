from classes.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome, "Professor")
        self.disciplina = disciplina

    def __str__(self):
        return f"Professor {self.nome} - {self.disciplina}"

    def acessar_cantina(self):
        return f"Professor {self.nome} acessa a cantina com crachá."