from fastapi.testclient import TestClient
from api import app


client = TestClient(app)

def test_criar_cotacao():
    dados = {
        "produto": "Papel A4",
        "quantidade": 10,
        "fornecedores": [
            {
                "Nome": "Fornecedor A",
                "Preço": 300
            },
            {
                "Nome": "Fornecedor B",
                "Preço": 200
            },
            {
                "Nome": "Fornecedor C",
                "Preço": 250
            }
        ]
    }

    response = client.post("/cotacoes", json=dados)

    assert response.status_code == 200

    resultado = response.json()

    assert resultado["produto"] == "Papel A4"
    assert resultado["quantidade"] == 10
    assert resultado["melhores_fornecedores"][0]["Nome"] == "Fornecedor B"
    assert resultado["melhores_fornecedores"][0]["Preço"] == 200

def test_quantidade_invalida():
    dados = {
        "produto": "Papel A4",
        "quantidade": -10,
        "fornecedores": [
            {
                "Nome": "Fornecedor A",
                "Preço": 200
            }
        ]
    }

    response = client.post("/cotacoes", json=dados)

    assert response.status_code == 422

def test_lista_fornecedores_vazia():
    dados = {
            "produto": "Papel A4",
            "quantidade": 10,
            "fornecedores": [
            ]
        }

    response = client.post("/cotacoes", json=dados)
    assert response.status_code == 422