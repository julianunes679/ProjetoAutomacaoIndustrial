from services.sistema_gestao import SistemaGestao

def exibir_menu():
    print("\n" + "="*45)
    print("  AUTOMAÇÃO INDUSTRIAL - GESTÃO DE QUALIDADE  ")
    print("="*45)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair do programa")
    print("="*45)

def ler_numero_positivo(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("❌ Por favor, digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")

def main():
    sistema = SistemaGestao()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-5): ").strip()

        if opcao == "1":
            print("\n--- CADASTRO DE PEÇA ---")
            id_peca = input("ID da Peça: ").strip()
            if not id_peca:
                print("❌ O ID da peça não pode ser vazio.")
                continue

            peso = ler_numero_positivo("Peso (g): ")
            cor = input("Cor (ex: azul, verde, vermelho): ").strip()
            comprimento = ler_numero_positivo("Comprimento (cm): ")

            sistema.cadastrar_peca(id_peca, peso, cor, comprimento)

        elif opcao == "2":
            sistema.listar_pecas()

        elif opcao == "3":
            print("\n--- REMOVER PEÇA ---")
            id_peca = input("Digite o ID da peça a ser removida: ").strip()
            if id_peca:
                sistema.remover_peca(id_peca)
            else:
                print("❌ ID inválido.")

        elif opcao == "4":
            sistema.listar_caixas_fechadas()

        elif opcao == "5":
            sistema.gerar_relatorio_final()

        elif opcao == "0":
            print("\nEncerrando o sistema de automação. Até logo!")
            break

        else:
            print("\n❌ Opção inválida! Escolha um número entre 0 e 5.")

if __name__ == "__main__":
    main()