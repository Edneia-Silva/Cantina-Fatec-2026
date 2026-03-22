from datetime import datetime

class Pagamento:
    def __init__(self, usuario, valor):
        self.usuario = usuario      # quem fez o pagamento
        self.valor = valor          # valor pago
        self.data_hora = datetime.now()  # registra automaticamente o momento

    def __str__(self):
        return f"{self.usuario.nome} ({self.usuario.categoria}) pagou R${self.valor:.2f} em {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}"