def encontrar_menor_preco(fornecedores):
  menor_preco = fornecedores[0]["Preço"]

  melhores_fornecedores = []

  for fornecedor in fornecedores:
    if fornecedor["Preço"] < menor_preco:
      menor_preco = fornecedor["Preço"]

  for fornecedor in fornecedores:
    if fornecedor["Preço"] == menor_preco:
      melhores_fornecedores.append(fornecedor)

  return melhores_fornecedores