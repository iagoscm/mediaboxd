<h1 align="center"> mediaboxd </h1>

# 📄 Sobre o projeto

O mediaboxd é um site para armazenamento e avaliação de filmes e séries assistidos, com o intuito de treinar e aprender o processo de desenvolvimento de software e as tecnologias usadas no mesmo

Projeto desenvolvido para a disciplina Desenvolvimento de Software da UnB - Campus Gama, ministrada pelo professor Sergio Antonio Andrade de Freitas

# 🤝 Colaboradores

|![Icaro](https://github.com/icarooliv.png) |![Luan](https://github.com/Luanmq.png)|![Iago](https://github.com/iagoscm.png)|
| - | - | - |
|[Icaro Oliveira](https://github.com/icarooliv)|[Luan Melo](https://github.com/Luanmq) | [Iago Campelo](https://github.com/iagoscm)|

|![William](https://github.com/WillAllmeida.png)|![Gabriel](https://github.com/gabrielvaraujo.png)|![Hellen](https://github.com/Hellen159.png)|![Henrique](https://github.com/HenriPucci.png)
| - | - | - | - |
|[William Almeida](https://github.com/WillAllmeida)|[Gabriel Araujo](https://github.com/gabrielvaraujo)|[Hellen Faria](https://github.com/Hellen159)|[Henrique Pucci](https://github.com/HenriPucci)|

# 📦 Releases

O projeto como um todo foi separado em duas releases, onde organizamos as User Stories de maneira equalitária para tentarmos entregar o máximo de requisitos possíveis em tempo hábil

<details>
<summary>Release 1</summary>

### Foco em conhecer as tecnologias, se ambientar com o processo ágil e implementar features

    - Dojos de Python
    - Dojos de Scrum/Ágil
    - Dojo de Django Básico
    - Dojo de Django Forms
    - Melhorar o protótipo
    - Configuração do projeto
    - US01 - Cadastro de usuário e admin
    - US02 - Login de usuário e admin
    - US03 - Adicionar review (usuário)
    - US06 - Atualizar review (usuário e admin)
    - US05 - Excluir review (usuário e admin)

</details>
<details>
<summary>Release 2</summary>

### Foco em pequenas melhorias nas features principais e conhecer mais do processo de ciclo de vida de um software
    - Dojo e implementação de testes
    - Deploy (Heroku)
    - Pareamento
    - Busca e filtragem
    - Adicionar tags e mídia
    - Correções visuais (CSS/HTML)
### Objetivos extras (não realizamos pois faltou tempo hábil)
    - Organizar playlists de conteúdos
    - Recomendações de mídias
    - Interação com as reviews de outros usuários

</details>

# ⚙️ Tecnologias utilizadas

As tecnologias foram escolhidas de acordo com as tecnologias utilizadas pelos mais experientes e mais fáceis para o aprendizado dos novatos.

| Frontend |	Backend | Framework | Infraestrutura (deploy) |
| - | - | - | - |
| ReactJS | Python | Django | Heroku |
### Banco de dados
| Nuvem |	Local | 
| - | - |
| PostgreSQL | SQLite |

<div style="display: inline_block">
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="react" width="50rem"/>
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="python" width="50rem"/>
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="django" width="50rem"/>
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-plain-wordmark.svg" alt="django" width="50rem"/>
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="50rem"/>
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="django" height="50" width="50"/>
</div>

# 💻 Como rodar 

## Pré-requisitos

Python 3.7.0 ou maior

## Criando ambiente virtual (Linux)

Execute os comandos no terminal, a partir do diretório `src`

Primeiro, crie um ambiente virtual:

`python -m venv myvenv` 

Depois, ative esse ambiente:

`source myvenv/bin/activate`

## Criando ambiente virtual (Windows)

Execute os comandos no terminal, a partir do diretório `src`

Primeiro, crie um ambiente virtual:

`python -m venv myvenv` 

Depois, ative esse ambiente:

`myvenv\Scripts\activate`

## Instalando pacotes e subindo o servidor

Em seguida, instale o Django 

`pip install -r requirements.txt`

E depois, faça as migrações base do Django

`python manage.py migrate`

Para subir o servidor, digite:

`python manage.py runserver`

O servidor deve estar disponível no endereço `http://localhost:8000`
