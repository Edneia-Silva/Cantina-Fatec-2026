from classes.usuario import Usuario

class Visitante(Usuario):
    def __init__(self, nome, documento):
        super().__init__(nome, "Visitante")
        self._documento = documento
    def acessar_cantina(self):
        return f"Visitante {self._nome} (Doc: {self._documento}) acessou."