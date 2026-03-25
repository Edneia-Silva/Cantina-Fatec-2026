class Usuario:
    def __init__(self, nome, categoria):
        self._nome = nome          # Atributo protegido (Encapsulamento)
        self._categoria = categoria

    @property
    def nome(self): 
        return self._nome

    def acessar_cantina(self):
        # Polimorfismo: todo usuário acessa, mas cada um do seu jeito
        return f"{self._nome} entrou na cantina."  

    @property
    def categoria(self): 
        return self._categoria