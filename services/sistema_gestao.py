from models.peca import Peca
from models.caixa import Caixa

class SistemaGestao:
    def __init__(self):
        self.pecas_cadastradas = []  # Armazena todas as peças (aprovadas e reprovadas)
        self.caixas = []  # Lista de caixas de armazenamento
        self._obter_ou_criar_caixa_atual()

    def _obter_ou_criar_caixa_atual(self) -> Caixa:
        """Retorna a caixa atual disponível ou cria uma nova se necessário."""
        if not self.caixas or self.caixas[-1].esta_cheia():
            nova_caixa = Caixa(numero_caixa=len(self.caixas) + 1)
            self.caixas.append(nova_caixa)
        return self.caixas[-1]

    def cadastrar_peca(self, id_peca: str, peso: float, cor: str, comprimento: float):
        """Cadastra uma nova peça, avalia e armazena na caixa se for aprovada."""
        # Verificar duplicidade de ID
        if any(p.id_peca == id_peca for p in self.pecas_cadastradas):
            print(f"\n❌ Erro: Já existe uma peça cadastrada com o ID '{id_peca}'.")
            return

        peca = Peca(id_peca, peso, cor, comprimento)
        self.pecas_cadastradas.append(peca)

        if peca.aprovada:
            caixa_atual = self._obter_ou_criar_caixa_atual()
            caixa_atual.adicionar_peca(peca)
            print(f"\n✅ Peça '{peca.id_peca}' APROVADA e armazenada na Caixa #{caixa_atual.numero_caixa}.")
            if caixa_atual.fechada:
                print(f"📦 A Caixa #{caixa_atual.numero_caixa} atingiu a capacidade máxima (10 peças) e foi FECHADA!")
        else:
            print(f"\n⚠️ Peça '{peca.id_peca}' REPROVADA!")
            for motivo in peca.motivos_reprovacao:
                print(f"   - {motivo}")

    def listar_pecas(self):
        """Lista todas as peças separadas por aprovadas e reprovadas."""
        if not self.pecas_cadastradas:
            print("\nℹ️ Nenhuma peça cadastrada até o momento.")
            return

        aprovadas = [p for p in self.pecas_cadastradas if p.aprovada]
        reprovadas = [p for p in self.pecas_cadastradas if not p.aprovada]

        print("\n--- 🟢 PEÇAS APROVADAS ---")
        if aprovadas:
            for p in aprovadas:
                print(p)
        else:
            print("Nenhuma peça aprovada.")

        print("\n--- 🔴 PEÇAS REPROVADAS ---")
        if reprovadas:
            for p in reprovadas:
                print(p)
        else:
            print("Nenhuma peça reprovada.")

    def remover_peca(self, id_peca: str):
        """Remove uma peça cadastrada do sistema e atualiza o armazenamento nas caixas."""
        peca_encontrada = None
        for p in self.pecas_cadastradas:
            if p.id_peca == id_peca:
                peca_encontrada = p
                break

        if not peca_encontrada:
            print(f"\n❌ Erro: Peça com ID '{id_peca}' não encontrada.")
            return

        # Remover da lista geral
        self.pecas_cadastradas.remove(peca_encontrada)

        # Se estava aprovada, remover da caixa
        if peca_encontrada.aprovada:
            for caixa in self.caixas:
                if peca_encontrada in caixa.pecas:
                    caixa.pecas.remove(peca_encontrada)
                    caixa.fechada = False  # Se a caixa estava fechada, volta a ficar aberta
                    break

        print(f"\n🗑️ Peça '{id_peca}' removida com sucesso do sistema!")

    def listar_caixas_fechadas(self):
        """Lista todas as caixas que já atingiram a capacidade máxima."""
        caixas_fechadas = [c for c in self.caixas if c.fechada]

        print("\n--- 📦 CAIXAS FECHADAS ---")
        if not caixas_fechadas:
            print("Nenhuma caixa fechada no momento.")
            return

        for c in caixas_fechadas:
            print(c)
            print("  Peças contidas:")
            for p in c.pecas:
                print(f"    - ID: {p.id_peca} | Cor: {p.cor.capitalize()}")

    def gerar_relatorio_final(self):
        """Gera um relatório consolidado com todas as métricas do sistema."""
        aprovadas = [p for p in self.pecas_cadastradas if p.aprovada]
        reprovadas = [p for p in self.pecas_cadastradas if not p.aprovada]
        caixas_fechadas = [c for c in self.caixas if c.fechada]

        print("\n==============================================")
        print("          RELATÓRIO FINAL CONSOLIDADO         ")
        print("==============================================")
        print(f"Total de peças analisadas : {len(self.pecas_cadastradas)}")
        print(f"Total de peças APROVADAS  : {len(aprovadas)}")
        print(f"Total de peças REPROVADAS : {len(reprovadas)}")
        print(f"Total de caixas UTILIZADAS: {len(self.caixas)}")
        print(f"Total de caixas FECHADAS  : {len(caixas_fechadas)}")
        print("----------------------------------------------")

        if reprovadas:
            print("\n📋 MOTIVOS DE REPROVAÇÃO DAS PEÇAS:")
            for p in reprovadas:
                print(f"• ID '{p.id_peca}':")
                for motivo in p.motivos_reprovacao:
                    print(f"   - {motivo}")
        else:
            print("\n✨ Nenhuma peça foi reprovada.")

        print("==============================================\n")