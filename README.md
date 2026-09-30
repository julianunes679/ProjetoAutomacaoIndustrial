Aqui está o conteúdo do arquivo **`README.md`** sem os blocos de código formatados com caixas, pronto para copiar diretamente:

# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Este projeto é um sistema lógico desenvolvido em Python para prototipar a automação do controle de produção, inspeção de qualidade e armazenamento de peças em uma linha de montagem industrial.

---

##  Funcionalidades

* **Cadastro de Peças:** Recebe o ID, peso (g), cor e comprimento (cm) de cada peça.
* **Inspeção Automática de Qualidade:** Avalia se a peça atende aos critérios pré-definidos:
* **Peso:** Entre 95g e 105g.
* **Cor:** Azul ou verde.
* **Comprimento:** Entre 10cm e 20cm.


* **Gestão de Armazenamento:**
* Armazena automaticamente apenas as peças aprovadas em caixas de capacidade máxima de 10 unidades.
* Ocorre o fechamento automático da caixa ao atingir a capacidade e abertura de uma nova.


* **Remoção de Peças:** Permite remover uma peça cadastrada, ajustando o estado das caixas de armazenamento.
* **Relatório Consolidado:** Gera métricas detalhadas do processo (peças aprovadas, reprovadas, motivos de rejeição e caixas utilizadas/fechadas).

---

##  Estrutura do Projeto

projetoAutomacaoIndustrial/

* models/
* **init**.py
* peca.py (Classe Peca e lógica de validação de qualidade)
* caixa.py (Classe Caixa e controle de capacidade)


* services/
* **init**.py
* sistema_gestao.py (Lógica de controle, armazenamento e relatórios)


* main.py (Interface do menu interativo via terminal)

---

##  Como Rodar o Programa

### Pré-requisitos

* Python 3.8 ou superior instalado no seu sistema.

### Passo a Passo

1. **Navegar até a pasta do projeto no terminal:**
cd projetoAutomacaoIndustrial
2. **Executar a Aplicação:**
python main.py

---

##  Exemplos de Entradas e Saídas

### 1. Cadastrar Peça Aprovada (Opção 1)

* **Entrada:** ID: P001 | Peso: 100 | Cor: azul | Comprimento: 15
* **Saída no Terminal:** ✅ Peça 'P001' APROVADA e armazenada na Caixa #1.

---

### 2. Cadastrar Peça Reprovada (Opção 1)

* **Entrada:** ID: P002 | Peso: 110 | Cor: vermelho | Comprimento: 8
* **Saída no Terminal:**
⚠️ Peça 'P002' REPROVADA!
* Peso fora do padrão (110.0g). Esperado: 95g a 105g.
* Cor inválida ('vermelho'). Esperadas: azul ou verde.
* Comprimento fora do padrão (8.0cm). Esperado: 10cm a 20cm.



---

### 3. Listar Caixas Fechadas (Opção 4)

* **Saída no Terminal:**
--- 📦 CAIXAS FECHADAS ---
Caixa #1 - Peças: 10/10 - Status: Fechada
Peças contidas:
- ID: P001 | Cor: Azul
- ID: P003 | Cor: Verde

---

### 4. Gerar Relatório Final (Opção 5)

* # **Saída no Terminal:**


```
      RELATÓRIO FINAL CONSOLIDADO         

```


## ==============================================
Total de peças analisadas : 2
Total de peças APROVADAS  : 1
Total de peças REPROVADAS : 1
Total de caixas UTILIZADAS: 1
Total de caixas FECHADAS  : 0


📋 MOTIVOS DE REPROVAÇÃO DAS PEÇAS:
• ID 'P002':
* Peso fora do padrão (110.0g). Esperado: 95g a 105g.
* Cor inválida ('vermelho'). Esperadas: azul ou verde.
* Comprimento fora do padrão (8.0cm). Esperado: 10cm a 20cm.
==============================================