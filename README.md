# MVP Gestão de Serviços de Limpeza

Projeto acadêmico desenvolvido na disciplina de Projeto de Software.

O objetivo deste MVP é centralizar a gestão de clientes, propriedades, profissionais e serviços de limpeza em uma aplicação web.

## Tecnologias

- Python
- Django
- Bootstrap
- PostgreSQL
- pytest

## Funcionalidades previstas

- Cadastro de clientes
- Cadastro de propriedades
- Cadastro de serviços
- Atribuição de profissionais
- Atualização do status dos atendimentos
- Agenda de serviços
- Controle de acesso por perfil

## Arquitetura

O projeto utiliza uma arquitetura monolítica em camadas, separando apresentação, lógica de negócio e persistência de dados.

## Status

Em desenvolvimento.

## Estrutura do MVP

O projeto utiliza Django com arquitetura monolítica em camadas. O app `core` concentra os modelos e fluxos principais do domínio, enquanto os templates reutilizam `base.html` para manter navegação, identidade visual e estrutura de página consistentes.

As telas principais do protótipo são:
- Agenda de serviços
- Cadastro de novo serviço
- Detalhes e acompanhamento do serviço

O banco PostgreSQL é utilizado para persistência e o projeto mantém separação entre configuração do projeto, regras do app e camada de apresentação.
