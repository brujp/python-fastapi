# Primeira utilização do framework FastAPI

Primeira utilização do framework Fast API - Implementação de uma "api" super simples com apenas dois recursos

Documentação do FastAPI: https://fastapi.tiangolo.com/

✅ Para acessar a documentação (Swagger), rodar a aplicação localmente e acessar: http://localhost:8000/docs

⏯ Para rodar a aplicação, foi utilizado o uvicorn como servidor local (uvicorn main:app --reload)

Utilizar o Postman ou Insomnia para realizar as requests!

⏬ GET /vendas

⏬ GET /vendas/{id_venda}

💾 Nosso "banco de dados" é apenas uma lista com 3 recursos:

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa", "preco_unitario": 7, "quantidade": 9},
    3: {"item": "lata mini", "preco_unitario": 3, "quantidade": 2}
}

https://www.youtube.com/watch?v=R26iojTwUv8
