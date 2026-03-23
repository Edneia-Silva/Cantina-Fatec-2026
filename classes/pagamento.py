from datetime import datetime

class Pagamento:
    def __init__(self, usuario, valor):
        self.usuario = usuario            # objeto Usuario (nome, categoria, curso)
        self.valor = valor                # valor pago
        self.data_hora = datetime.now()   # registra automaticamente o momento
        self.metodo = "PIX"               # forma de pagamento (fixo no projeto)

    def __str__(self):
        return (f"Pagamento: {self.usuario.nome} ({self.usuario.categoria}, {self.usuario.curso}) "
                f"pagou R${self.valor:.2f} via {self.metodo} em {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}")