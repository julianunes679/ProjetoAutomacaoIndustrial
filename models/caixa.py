class Caixa:
    CAPACIDADE_MAXIMA = 10

    def __init__(self, numero_caixa: int):
        self.numero_caixa = numero_caixa
        self.pecas = []
        self.fechada = False

    def adicionar_peca(self, peca) -> bool:
        """Adiciona uma peça à caixa caso não esteja fechada e haja espaço."""
        if self.fechada:
            return False

        if len(self.pecas) < self.CAPACIDADE_MAXIMA:
            self.pecas.append(peca)
            if len(self.pecas) == self.CAPACIDADE_MAXIMA:
                self.fechada = True
            return True
        return False

    def esta_cheia(self) -> bool:
        return len(self.pecas) >= self.CAPACIDADE_MAXIMA

    def __str__(self):
        status = "Fechada" if self.fechada else "Aberta (Em uso)"
        return f"Caixa #{self.numero_caixa} - Peças: {len(self.pecas)}/{self.CAPACIDADE_MAXIMA} - Status: {status}"