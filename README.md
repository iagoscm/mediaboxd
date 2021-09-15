# ds-top-5
Um trabalho feito com muito amor e carinho

Integrantes da equipe:
- Gabriel Araújo
- Luan Melo
- Ícaro Pereira
- William Almeida
- Iago Campelo
- Hellen Faria
- Henrique Pucci

print('Hello, world!')


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
