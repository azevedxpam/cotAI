from cotacao import encontrar_menor_preco

def test_encontrar_menor_preco():
  fornecedores = [
        {"Nome": "Fornecedor A", "Preço": 300},
        {"Nome": "Fornecedor B", "Preço": 200},
        {"Nome": "Fornecedor C", "Preço": 250}
    ]

  resultado = encontrar_menor_preco(fornecedores)

  assert resultado[0]["Nome"] == "Fornecedor B"
  assert resultado[0]["Preço"] == 200

def test_menor_preco_no_ultimo_fornecedor():
    fornecedores = [
        {"Nome": "Fornecedor A", "Preço": 300},
        {"Nome": "Fornecedor B", "Preço": 250},
        {"Nome": "Fornecedor C", "Preço": 100}
    ]

    resultado = encontrar_menor_preco(fornecedores)

    assert resultado[0]["Nome"] == "Fornecedor C"
    assert resultado[0]["Preço"] == 100

def test_empate_no_menor_preco():
    fornecedores = [
        {"Nome": "Fornecedor A", "Preço": 200},
        {"Nome": "Fornecedor B", "Preço": 200},
        {"Nome": "Fornecedor C", "Preço": 300}
    ]

    resultado = encontrar_menor_preco(fornecedores)

    assert len(resultado) == 2
    assert resultado[0]["Nome"] == "Fornecedor A"
    assert resultado[1]["Nome"] == "Fornecedor B"