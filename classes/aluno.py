from classes.usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, curso):
        super().__init__(nome, "Aluno") # Envia para a 'mãe'
        self._curso = curso
        
    def acessar_cantina(self):
        return f"Aluno {self._nome} do curso {self._curso} acessou."