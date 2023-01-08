#Uvicorn - Servidor local
from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa", "preco_unitario": 7, "quantidade": 9},
    3: {"item": "lata mini", "preco_unitario": 3, "quantidade": 2}
}

@app.get("/vendas")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}