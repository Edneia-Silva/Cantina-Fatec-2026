class Professor:
    def _init_(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def _str_(self):
        return f"Professor {self.nome} - {self.disciplina}"