from fastapi import FastAPI
import uvicorn

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2l", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

@app.get("/")
def root():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
     if id_venda in vendas:
        return vendas[id_venda]
     else:
        return {"Error": "ID venda inexistente"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)