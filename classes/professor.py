from classes.usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, disciplina):
        super().__init__(nome, "Professor")
        self._disciplina = disciplina

    def acessar_cantina(self):
        return f"Professor {self._nome} (Doc: {self._disciplina}) acessou."