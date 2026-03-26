# Sistema de Gestão: Cantina Fatec Rio Claro

Este projeto consiste em um sistema de gerenciamento de estoque e vendas para uma cantina acadêmica. Desenvolvido como projeto final para as disciplinas de **Linguagem de Programação II** e **Estrutura de Dados** do curso de **Inteligência Artificial (IA)**.


**Orientador:** Prof. Orlando Saraiva Jr.

---

## Funcionalidades principais
**Gestão de Estoque Inteligente**: Implementação manual de uma **Lista Encadeada** para organizar produtos por data de vencimento, utilizando a lógica **PVPS** (Primeiro que Vence, Primeiro que Sai).
**Controle de Fluxo**: registro automatizado de vendas com baixa imediata e real no estoque.
**Sistema de Pagamento**: registro de transações via **PIX**, com diferenciação polimórfica entre categorias (Aluno, Professor, Servidor e Visitante).
**Persistência de Dados**: utilização da biblioteca `pickle` para armazenamento binário (não volátil), garantindo a continuidade dos dados.
**Simulação Realista**: população do sistema com dados brasileiros aleatórios (nomes, documentos e cursos) via biblioteca `Faker`.

---

## Tecnologias utilizadas
* **Linguagem**: Python 3.14
* **Bibliotecas**: 
    * `Faker`: geração de massas de dados.
    * `pickle`: persistência de objetos.
    * `datetime`: manipulação de cronogramas e validades.

---

## Estrutura do Projeto
O sistema foi desenhado seguindo os pilares da **Programação Orientada a Objetos (POO)**:
* **`main.py`**: orquestrador do sistema e fluxo de execução.
* **`classes/`**:
    * `estrutura_dados.py`: core do sistema (`No` e `ListaEncadeada`).
    * `relatorio.py`: módulo de BI para consolidação de dados financeiros.
    * `usuario.py`: classe base com **Encapsulamento** e **Getters/Setters**.
    * `aluno.py`, `professor.py`, `servidor.py`, `visitante.py`: especializações via **Herança** e **Polimorfismo**.
    * `produto.py`: entidade de representação dos itens e controle de perecíveis.
    * `estoque.py`: gerenciador de lógica da Lista Encadeada.
    * `venda.py` & `pagamento.py`: módulos de controle financeiro.
     **`estoque_cantina.pkl`**: base de dados serializada.

---

## Resultados da Simulação (Versão Final)
O sistema foi validado com um fluxo de **10 transações simultâneas**, apresentando:
✅ Baixa automática de estoque (zerando itens de alta rotatividade).
✅ Persistência confirmada de **R$ 119,00** em faturamento bruto.
✅ Identificação precisa de perfis de consumo.

### Log de Execução Exemplo:
```text
--- Processando Fluxo de Vendas (10 transações) ---
Venda confirmada: 2x Coxinha para Isabel Martins.
Venda confirmada: 3x Pão de Queijo para Sr. Davi Luiz Jesus.
...
[Sistema] Dados salvos com sucesso via Pickle!

--- Gerando Relatórios Finais ---

==================================================
📊 RELATÓRIO FINANCEIRO - CONSOLIDADO
==================================================
ID    | Cliente            | Valor (R$) | Metodo
--------------------------------------------------
101   | Isabel Martins     | 16.00      | PIX
102   | Sr. Davi Luiz Jesu | 15.00      | PIX
...
110   | Isabel Martins     | 7.50       | PIX
--------------------------------------------------
💰 FATURAMENTO TOTAL: R$ 119.00
==================================================

---

🟦 Desenvolvido por **Ednéia Silva** - Estudante de Inteligência Artificial | Fatec Rio Claro (2026)



