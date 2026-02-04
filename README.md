
# Projeto1-API_com_Docker

API simples em Flask containerizada com Docker.

## 🎯 Objetivo
Praticar Docker do zero criando uma API mínima com:
- endpoint de home (`/`)
- endpoint de health check (`/health`)
- build e execução via Docker

## 🧰 Tecnologias
- Python 3.12
- Flask
- Docker

## 📦 Como rodar com Docker

### 1) Build da imagem
```bash
docker build -t api-flask .
````

### 2) Rodar o container

```bash
docker run --name api-flask -p 8000:8000 api-flask
```

Acesse:

* [http://localhost:8000](http://localhost:8000)
* [http://localhost:8000/health](http://localhost:8000/health)

## 🛑 Parar e remover

```bash
docker stop api-flask
docker rm api-flask
```


