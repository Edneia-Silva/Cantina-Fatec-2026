# Cantina-Fatec-2026

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


