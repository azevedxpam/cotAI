fornecedores = [
  {
    "Nome": "Fornecedor A",
    "Preço": 250
  },
  {
    "Nome": "Fornecedor B",
    "Preço": 220
  },
  {
    "Nome": "Fornecedor C",
    "Preço": 270
  },
  {
    "Nome": "Fornecedor D",
    "Preço": 200
  }
  ]

for fornecedor in fornecedores:
  print(fornecedor["Nome"], "→ R$", fornecedor["Preço"])

menor_preco = fornecedores[0]

for fornecedor in fornecedores:
  if fornecedor["Preço"] < menor_preco["Preço"]:
    menor_preco = fornecedor

print()
print("===== MELHOR COTAÇÃO =====")
print("Fornecedor:", menor_preco["Nome"])
print("Preço: R$", menor_preco["Preço"])