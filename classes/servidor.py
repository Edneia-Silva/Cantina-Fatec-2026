from classes.usuario import Usuario

class Servidor(Usuario):
    def __init__(self, nome, setor):
        super().__init__(nome, "Servidor")
        self._setor = setor

    def acessar_cantina(self):
        return f"Servidor {self._nome} (Doc: {self._setor}) acessou."