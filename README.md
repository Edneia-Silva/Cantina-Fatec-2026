# Cantina-Fatec-2026

Este projeto simula o funcionamento de uma cantina acadêmica, com controle de estoque, vendas e pagamentos.

## Commit 1
- Estrutura inicial do projeto criada.
- Implementei apenas a classe **Aluno**, que representa os usuários da Cantina Fatec neste primeiro momento.
- Testei no `main.py` criando dois objetos de alunos.
- Próximos commits vão incluir **Professor** e **Servidor** como novas categorias. Talvez inclua **Visitante** já que outras pessoas podem comprar na cantina, basta pagar.

## Commit 2
- Alterei os nomes dos alunos para Roger e Brianna.

## Commit 3
- Adicionei as classes **Professor** e **Servidor**.
- Agora o sistema permite representar diferentes categorias de pessoas que usam a cantina.
- Testei no `main.py` criando objetos de cada categoria.

## Commit 4
- Corrigi um erro na classe Aluno: o método __init__ estava escrito errado.
- Agora a classe aceita argumentos corretamente (nome, matrícula e curso).
- Testei no main.py criando dois objetos (Roger e Brianna) e funcionou.

## Commit 5
- Criei a classe **Visitante** para representar pessoas de fora da Fatec que também podem usar a cantina quando visitam a unidade.
- Agora o sistema contempla quatro categorias: Aluno, Professor, Servidor e Visitante.
- Testei no `main.py` criando objetos de cada categoria.

## Commit 6
- Criei o arquivo __init__.py para transformar a pasta `classes` em um pacote Python.
- Refatorei o código criando a classe base **Pessoa**.
- Agora **Aluno**, **Professor**, **Servidor** e **Visitante** herdam de Pessoa.
- Essa refatoração aplica os conceitos de **herança e polimorfismo** da disciplina de LP II.
- Testei no `main.py` e todos os objetos funcionaram corretamente.

## Commit 7
- Adicionei o método acessar_cantina() na classe base Pessoa.
- Sobrescrevi o método em Aluno, Professor, Servidor e Visitante.
- Usei polimorfismo: cada classe acessa a cantina de forma diferente.
- Testei no main.py percorrendo uma lista de pessoas.

## Commit 8 – Classe Produto
- Criei a classe Produto para representar os itens da cantina.
- Apliquei encapsulamento, pois o controle de estoque está dentro da classe.
- Também usei datetime para manipular datas de compra e vencimento.

## Commit 9 – Renomeando classe Pessoa para Usuário
- Alterei o nome da classe base de Pessoa para Usuario, pois faz mais sentido no contexto da cantina.
- Renomeei o arquivo pessoa.py para usuario.py
- Mantive o uso de herança para representar diferentes tipos de usuários (Aluno, Professor, Servidor, Visitante).
- Atualizei todos os imports nos demais arquivos
- Ajustei as subclasses (Aluno, Professor, Servidor, Visitante) para herdarem de Usuario
- Testei o código e confirmei que funciona corretamente

## Commit 10 – Criando classe Estoque
- Criei a classe Estoque para gerenciar todos os produtos da cantina
- Adicionei métodos para adicionar, listar e buscar produtos
- Testei com exemplos simples (coxinha e suco)
- Essa etapa mostra o uso de **estruturas de dados** (lista) para organizar os produtos

## Commit 11 – Criando arquivo testes.py
- Criei arquivo separado para validar classes (Produto e Estoque)
- Mantive o main.py apenas para execução principal do sistema
- Testes.py permite rodar exemplos isolados sem interferir no fluxo principal (main.py)

## Commit 12 – Criando classe Pagamento
- Criei a classe Pagamento para registrar transações financeiras
- A classe guarda o usuário, valor pago e data/hora automática
- Testei no arquivo testes.py com um exemplo de aluno pagando R$7,50
- Esse passo mostra o uso de **encapsulamento** e integração entre classes (Usuario e Pagamento)

## Commit 13 – Testando subclasses de Usuario
- Ajustei usuario.py com as subclasses Aluno, Professor, Servidor e Visitante
- Criei teste simples em testes.py para validar instâncias
- Corrigi erro de import no testes.py
- Confirmado que os imports funcionam e as classes retornam corretamente

## Commit 14 – Criando classe Venda
- Criei a classe Venda para representar uma operação completa de compra
- Venda conecta Usuario, Produto e Pagamento em uma única transação
- Adicionei atributos: quantidade, valor total e data/hora
- Testei no arquivo testes.py com exemplo de aluno comprando 2 coxinhas 

## Commit 15 – Implementando controle de vencimento
- Ajustei Estoque para verificar data de vencimento antes da venda
- Produtos vencidos são removidos automaticamente e não podem ser vendidos
- Mantive a lógica FIFO para consumir primeiro os itens mais antigos
- Testei com produtos vencidos e válidos para confirmar o funcionamento

## Commit 16 – Incrementando controle de pagamento
- Adicionei campo metodo fixo como PIX na classe Pagamento
- Ajustei __str__ para exibir também o curso do usuário
- Mantive os campos já existentes (usuário, valor, data/hora)
- Testei integração com Venda para gerar pagamento automaticamente

## Commit 17 – Integração de Venda com Pagamento
- Ajustei __str__ da classe Venda para exibir também o pagamento
- Mantive a lógica de consumo FIFO e validação de estoque
- Testei com diferentes usuários para confirmar integração completa

## Commit 18 – Edição de quantidade em estoque
- Adicionei o método `editar_quantidade` na classe `Estoque`. 
- Permite atualizar a quantidade de um produto já existente sem rcriar o objeto.
- Caso o produto não seja encontrado, retorna uma mensagem informando.  
- Validado no arquivo `TesteCantina.py` criado na raiz do projeto.

## Commit 19 – Geração de dados aleatórios com Faker
- Implementada a biblioteca Faker para gerar dados fictícios e automatizar testes.
- Foram criados exemplos de alunos, produtos e vendas com informações aleatórias, como:  
    - Nome de aluno (ex.: João, Alex, Alana).  
    - Produto com nome, preço e quantidade.  
    - Data e hora da venda.  
    - Forma de pagamento simulada.  
- Essa funcionalidade facilita a validação do sistema sem precisar cadastrar manualmente cada item.  
- Os testes foram centralizados no arquivo `TesteCantina.py`, que agora também utiliza dados aleatórios para simular cenários reais.

## Commit 20 – Persistência de dados e Relatórios
- Implementada a utilização da biblioteca pickle para armazenar dados de forma não volátil, permitindo salvar e carregar posteriormente o estoque e as vendas.
- Criadas funções de relatórios de vendas e relatórios de consumo, possibilitando visualizar:todas as transações realizadas e quantidade de produtos consumidos em cada venda.
- Agora o sistema não apenas gera dados aleatórios com Faker, mas também mantém histórico e apresenta relatórios completos.

## Commit 21 - Cria classe EstruturaEstoque para encapsular lista de produtos
-  Criação da classe EstruturaEstoque.
- Encapsulamento de uma lista interna para armazenar produtos.
- Implementação de métodos próprios para manipulação dos dados.
- Preparação para substituir o uso direto de listas no controle de estoque.

## Commi 22 - Refatora classe Estoque para utilizar EstruturaEstoque
- Substituição do uso direto de lista por EstruturaEstoque
- Atualização dos métodos para utilizar a nova estrutura
- Adequação ao encapsulamento de dados

## Commit 23: Refatoração estrutural e implementação de lista encadeada
Realizei uma mudança profunda na forma como o estoque é armazenado pelos seguintes motivos:
1.	Conformidade com os requisitos: o projeto exige o desenvolvimento de estruturas de dados próprias. Substituí o uso de listas nativas [] por uma Lista Encadeada manual (com classes No e ListaEncadeada), eliminando o uso de funções prontas como .sort(). 
2.	Lógica PVPS (Primeiro que Vence, Primeiro que Sai): como a cantina lida com produtos perecíveis (coxinhas, sucos, industrializados), a nova estrutura insere os produtos já ordenados pela data de vencimento. 
3.	Encapsulamento: apliquei o conceito de atributos protegidos e métodos de acesso (Getters/Setters) para garantir que dados sensíveis, como a quantidade em estoque, não sejam alterados de forma indevida.
