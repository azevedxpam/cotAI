from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from cotacao import encontrar_menor_preco


app = FastAPI()

class Fornecedor(BaseModel):
    Nome: str
    Preço: float = Field(gt=0)


class Pedido(BaseModel):
    produto: str = Field(min_length=1)
    quantidade: int = Field(gt=0)
    fornecedores: list[Fornecedor] = Field(min_length=1)

    @field_validator("produto")
    @classmethod
    def validar_produto(cls, produto):
        produto = produto.strip()

        if not produto:
            raise ValueError("O produto não pode estar vazio.")

        return produto

@app.get("/")
def inicio():
    return {"mensagem": "CotAI está funcionando!"}

@app.post("/cotacoes")
def criar_cotacao(pedido: Pedido):

    fornecedores = [
        fornecedor.model_dump()
        for fornecedor in pedido.fornecedores
    ]

    resultado = encontrar_menor_preco(fornecedores)

    return {
        "produto": pedido.produto,
        "quantidade": pedido.quantidade,
        "melhores_fornecedores": resultado
    }