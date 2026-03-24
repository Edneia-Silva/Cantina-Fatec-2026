from datetime import datetime

class Pagamento:
    def __init__(self, usuario, valor):
        self._usuario = usuario
        self._valor = valor
        self._data_hora = datetime.now()
        self._metodo = "PIX"  # Fixo conforme a regrado projeto

    @property
    def valor(self): return self._valor

    def __str__(self):
        # Exibe o curso se for Aluno, ou categoria para os demais usuários
        info_extra = getattr(self._usuario, 'curso', self._usuario.categoria)
        return f"Pagamento de R${self._valor:.2f} confirmado via {self._metodo} para {self._usuario.nome} ({info_extra})."