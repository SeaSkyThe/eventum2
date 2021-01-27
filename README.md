![Django](https://img.shields.io/badge/Django-3.1.5-green)

# eventum
## Trabalho Semestral da disciplina de Banco de Dados II

A linguagem utilizada nesse projeto é Python 3.
#### Ativar o virtual environment antes de começar a editar o projeto.
1. Navegue até a pasta principal do projeto "eventum" pelo seu terminal.
2. Execute: "source myenv/bin/activate".
3. Para desativar o vevn digite "deactivate".


#### Rodar o projeto, e verificar se está funcionando.
1. Pode-se aplicar as migrations antes (atualizações no banco), fazendo "python manage.py migrate".
2. Ou, utilize diretamente "python manage.py runserver", e se o "migrate" for necessário, será avisado para você. O django é bonzinho!!


Uma introdução bacana ao Django, com um resuminho sobre o que é cada parte.
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction

## Configuração do banco de dados

Antes de mais nada, é preciso ter o MySQL [instalado](https://www.mysql.com/downloads/) na máquina e rodando (ex.: `brew services start mysql` para MAC).

São necessários os seguintes passos:

1. ```pip install mysqlclient```
2. ```mysql -u root -p``` (aqui você deve colocar a senha do MySQL, provavelmente criou ela quando o instalou em algum momento de sua vida)

3. Em seguida, execute os seguintes comandos do MySQL para criar o banco de dados e o usuário *djangouser*:

``` sql
CREATE DATABASE eventum;
```
``` sql
CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
```
``` sql
GRANT ALL ON eventum.* TO 'djangouser'@'%';
```
``` sql
FLUSH PRIVILEGES;
```
``` sql
EXIT;
```
Neste ponto, foi criado um usuário novo (login: djangouser, senha: password) no MySQL com permissão para usar o banco eventum.

Pode ser necessário criar um usuário no django (python manage.py createsuperuser) com as mesmas credenciais: login: djangouser, senha: password.

As migrações (makemigrations e migrate) e o conector (instalado em 1.) já estão no projeto e, provavelmente, não será necessário fazer novamente.
