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

# ⚙️ Tecnologias utilizadas

As tecnologias foram escolhidas de acordo com as tecnologias utilizadas pelos mais experientes e mais fáceis para o aprendizado dos novatos.

| Frontend |	Backend | Framework | Infraestrutura (deploy)
| - | - | - | - |
| ReactJS | Python | Django | Heroku |
### Banco de dados
| Nuvem |	Local | 
| - | - |
| PostgreSQL | SQLite |



## Como rodar 

Para a criação do ambiente virtual, prossiga de acordo com seu
sistema operacional.

### Criando ambiente virtual (Linux)
Execute os comandos no terminal, a partir do diretório `src`

Primeiro, crie um ambiente virtual:

`python -m venv myvenv` 

Depois, ative esse ambiente:

`source myvenv/bin/activate`


### Criando ambiente virtual (Windows)

Execute os comandos no terminal, a partir do diretório `src`

Primeiro, crie um ambiente virtual:

`python -m venv myvenv` 

Depois, ative esse ambiente:

`myvenv\Scripts\activate`


### Instalando pacotes e subindo o servidor

Em seguida, instale o Django 

`pip install -r requirements.txt`

E depois, faça as migrações base do Django

`python manage.py migrate`

Para subir o servidor, digite:

`python manage.py runserver`


O servidor deve estar disponível no endereço `http://localhost:8000`


## Pré-requisitos

Python 3.7.0 ou maior
