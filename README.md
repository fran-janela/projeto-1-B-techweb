<div align="center">
<h1>
  <strong>Projeto 1-B - TechWeb</strong>
</h1>
  
## Autor: 
  
<table>
  <tr>
    <td align="center"><a href="https://github.com/fran-janela"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/21694400?v=4" width="100px;" alt=""/><br /><sub><b>Francisco Pinheiro Janela</b></sub></a><br /><a href="https://github.com/fran-janela" title="Francisco Pinheiro Janela"></a></td>
    </tr>
</table>
  </br></br>
  
## Deploy da aplicação:
  
<p>para acessar o aplicativo <a href="https://morning-wave-79409.herokuapp.com/">clique aqui</a>.</br></br></p>
<p>Ou acesse o link abaixo:</p>
<a href="https://morning-wave-79409.herokuapp.com/">https://morning-wave-79409.herokuapp.com/</a>
</div>
</br></br></br></br>

## O que foi feito:

- [x] Aplicação em Django - com CRUD implementado e sistema de Tags
- [x] Base de dados em postgres
- [x] Deploy da aplicação no Heroku

## Adicionais:

- [x] Cores código para as tags 
- [x] Filtro JavaScript para visualizar uma cor específica em tags

</br></br>

# Ambiente de desenvolvimento

## Criando o ambiente:

Inicie um ambiente virtual:
```cmd
python -m venv venv
```

Ative o env:
```cmd
source venv/bin/activate
```

Instale as bibliotecas e frameworks necessários:
```cmd
pip install -r requirements.txt
```

## Criando a base de Dados:

Instale a imagem do Postgres:
```cmd
docker pull postgres
mkdir -p $HOME/docker/volumes/postgres
```

Crie a Base de Dados Postgres pelo docker:
```cmd
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=getitsenha -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
```

Acessando a Base de dados e executando autorizações:
```cmd
docker exec -it pg-docker bash
```

```cmd
psql -h localhost -U postgres
```

```cmd
CREATE DATABASE getit;
CREATE USER getituser WITH PASSWORD 'getitsenha';
ALTER ROLE getituser SET client_encoding TO 'utf8';
ALTER ROLE getituser SET default_transaction_isolation TO 'read committed';
ALTER ROLE getituser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE getit TO getituser;
\q
```

## Finalizando:

Rode as migrações para a base de dados:
```cmd
python manage.py makemigrations
python manage.py migrate
```

Inicie a aplicação:
```cmd
python manage.py runserver
```

<div align="right">
  Insper - 4ºComp
</div>
