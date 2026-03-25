# Sistema de Gestão da Cantina Fatec 

Este projeto consiste em um sistema de gerenciamento de estoque e vendas para uma cantina acadêmica, desenvolvido como parte da disciplina de **Linguagem de Programação II** e **Estrutura de Dados**, do curso de Inteligência Artificial (IA).

## Funcionalidades principais:
- **Gestão de estoque inteligente**: implementação manual de uma **Lista Encadeada** para organizar produtos por data de vencimento (Lógica PVPS - Primeiro que Vence, Primeiro que Sai).
- **Controle de consumo e vendas**: registro automatizado de vendas com baixa imediata no estoque.
- **Sistema de pagamento acadêmico**: registro de transações via **PIX**, diferenciando categorias (Aluno, Professor, Servidor e Visitante) e cursos (IA ou ESG).
- **Persistência de dados**: utilização da biblioteca `pickle` para armazenamento não volátil, garantindo que os dados não sejam perdidos ao fechar o sistema.
- **Simulação realista**: geração de dados aleatórios de usuários e documentos utilizando a biblioteca `Faker`.

## Tecnologias utilizadas:
- **Python 3.14**
- **Bibliotecas**: `Faker` (geração de dados), `pickle` (persistência), `datetime` (controle temporal).

## Estrutura do projeto (Versão Final)
- **`main.py`**: ponto de entrada que integra a simulação de acessos e o fluxo de vendas.
- **`classes/`**:
  - `estrutura_dados.py`: implementação das classes `No` e `ListaEncadeada`.
  - `usuario.py`: classe base com **Encapsulamento** e **Getters/Setters**.
  - `aluno.py`, `professor.py`, `servidor.py`, `visitante.py`: especializações via **Herança** e **Polimorfismo**.
  - `produto.py`: representação dos itens com controle de perecíveis.
  - `estoque.py`: gerenciador que opera a lógica da Lista Encadeada.
  - `venda.py` & `pagamento.py`: módulos de controle financeiro e baixa de estoque.
- **`estoque_cantina.pkl`**: base de dados serializada.

## Exemplo de execução (Log do Sistema):
Ao iniciar o sistema, o `main.py` realiza a simulação completa:
1. **Acesso**: o `Faker` gera um usuário (ex: Beatriz Abreu, Aluna de IA).
2. **Venda**: o sistema busca o produto "Coxinha" na **Lista Encadeada**.
3. **Baixa**: o estoque é atualizado (ex: de 50 para 48 unidades).
4. **Pagamento**: um objeto `Pagamento` é criado com o valor total e o método PIX.
5. **Persistência**: o `pickle` salva o estado atual no arquivo `.pkl`.

**Saída do terminal:**
--- Simulação de Acesso (Polimorfismo) ---
Aluno Beatriz Abreu do curso Inteligência Artificial acessou.

--- Realizando Venda ---
Venda confirmada: 2x Coxinha para Beatriz Abreu.
RECIBO: Beatriz Abreu | Total: R$16.00 | Pago via PIX

[Sistema] Dados salvos com sucesso em estoque_cantina.pkl!

## Requisitos atendidos (Checklist):
- [x] **POO**: uso de Herança, Polimorfismo e Encapsulamento.
- [x] **Estrutura de Dados**: Lista Encadeada implementada manualmente.
- [x] **Relatórios**: histórico de pagamentos com nome, categoria, curso e valor.
- [x] **Persistência**: dados salvos em arquivo binário.
- [x] **Faker**: população do sistema com dados brasileiros aleatórios.

---
Desenvolvido por **Edneia Silva** - Estudante de Inteligência Artificial | Fatec Rio Claro (2026)