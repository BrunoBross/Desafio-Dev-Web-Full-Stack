# Desafio Dev Web Full Stack @ Laboratório Bridge
### CTC | UFSC

### • Apresentação

### Olá!

O projeto a ser apresentado a seguir trata-se de um desafio para vaga de Desenvolvedor Full-Stack do @laboratório-bridge. Consiste em um *WebApp* que recebe um número real X > 100 do usuário e retorna o menor *Duodigito* múltiplo de X. O projeto além de verificar, mantém um histórico das verificações realizadas.

### • Especificações

O *Frontend* do projeto foi desenvolvido em HTML+CSS, com a utilização do framework [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/).

Já o *Backend* foi desenvolvido em Python, com a utilização do framework [Django](https://www.djangoproject.com/start/overview/). Também foi utilizado o [Sqlite3](https://www.sqlite.org/about.html) (padrão django) no banco de dados.

### • Execução Local do Projeto

Certifique-se que você tem o pip no seu terminal, caso esteja utilizando windows instale o [pip](https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/).

No seu terminal, execute os comandos na seguinte ordem:
> git clone https://github.com/BrunoBross/Desafio-Dev-Web-Full-Stack.git

> pip install django

Dentro da pasta do projeto execute:

> python manage.py runserver

Assim que executado, aparecerá no terminal um link de acesso local do app, mas você pode também acessar diretamente no seu navegador com [https://localhost:8000](https://localhost:8000)

### • Demo Online
 
Está disponível uma demonstração online para descartar a necessidade de rodar o projeto em um servidor local.

OBS: como se trata de uma hospedagem grátis (pouco processamento), pode haver algum delay no servidor quando feito testes maiores.

[Demo Heroku](https://dev-bridge.herokuapp.com/)
