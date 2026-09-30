class Peca:
    def __init__(self, id_peca: str, peso: float, cor: str, comprimento: float):
        self.id_peca = id_peca
        self.peso = peso
        self.cor = cor.strip().lower()
        self.comprimento = comprimento
        self.aprovada = False
        self.motivos_reprovacao = []
        
        self._avaliar_qualidade()

    def _avaliar_qualidade(self):
        """Avalia se a peça atende aos critérios de qualidade pré-definidos."""
        # Critério 1: Peso entre 95g e 105g
        if not (95 <= self.peso <= 105):
            self.motivos_reprovacao.append(f"Peso fora do padrão ({self.peso}g). Esperado: 95g a 105g.")

        # Critério 2: Cor azul ou verde
        if self.cor not in ["azul", "verde"]:
            self.motivos_reprovacao.append(f"Cor inválida ('{self.cor}'). Esperadas: azul ou verde.")

        # Critério 3: Comprimento entre 10cm e 20cm
        if not (10 <= self.comprimento <= 20):
            self.motivos_reprovacao.append(f"Comprimento fora do padrão ({self.comprimento}cm). Esperado: 10cm a 20cm.")

        # Aprovada se não houver motivos de reprovação
        self.aprovada = len(self.motivos_reprovacao) == 0

    def __str__(self):
        status = "Aprovada" if self.aprovada else "Reprovada"
        info = f"ID: {self.id_peca} | Peso: {self.peso}g | Cor: {self.cor.capitalize()} | Comprimento: {self.comprimento}cm | Status: {status}"
        if not self.aprovada:
            info += f" | Motivos: {'; '.join(self.motivos_reprovacao)}"
        return info