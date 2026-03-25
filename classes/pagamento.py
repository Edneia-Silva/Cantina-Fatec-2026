from datetime import datetime

class Pagamento:
    def __init__(self, usuario, valor):
        self._nome = usuario.nome
        self._categoria = usuario.categoria
        self._valor = valor
        self._data_hora = datetime.now()
        
        # Lógica para capturar a "Info Extra" (Curso, Setor, Disciplina ou Documento)
        if hasattr(usuario, '_curso'):
            self._detalhe = f"Curso: {usuario._curso}"
        elif hasattr(usuario, '_setor'):
            self._detalhe = f"Setor: {usuario._setor}"
        elif hasattr(usuario, '_disciplina'):
            self._detalhe = f"Disc: {usuario._disciplina}"
        else:
            self._detalhe = f"Doc: {getattr(usuario, '_documento', 'N/A')}"

    def __str__(self):
        data_f = self._data_hora.strftime("%d/%m/%Y %H:%M")
        return (f"[{data_f}] {self._nome} ({self._categoria}) | "
                f"{self._detalhe} | Valor: R${self._valor:.2f} | Metodo: PIX")