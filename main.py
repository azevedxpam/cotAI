def apresentar():
  print("Olá, eu sou o CotAI!")

def encontrar_menor_preco(fornecedores):
  menor_preco = fornecedores[0]

  for fornecedor in fornecedores:
    if fornecedor["Preço"] < menor_preco["Preço"]:
      menor_preco = fornecedor

  return menor_preco

def ler_preco():
  while True:
    try: 
      entrada = input("Preço: R$ ")
      entrada = entrada.replace(",", ".")
      preco = float(entrada)
      if preco >0:
        return preco
      print("O preço precisa ser maior que zero.")

    except ValueError:
      print("Informe um preço válido.")


def cadastrar_fornecedores():

  while True:
    try:
      quantidade_fornecedores = int(input("Com quantos fornecedores você quer fazer a cotação? "))

      if quantidade_fornecedores >0:
        break

      print("A quantidade deve ser maior do que 0.")  

    except ValueError:
      print("Digite uma quantidade válida.")
  fornecedores = []

  for i in range(quantidade_fornecedores):
    print()
    print("Fornecedor", i+1)

    nome = input("Nome: ")
    preco = ler_preco()

    fornecedor = {
      "Nome": nome,
      "Preço": preco
    }

    fornecedores.append(fornecedor)

  return fornecedores

apresentar()
fornecedores = cadastrar_fornecedores()
print()

for fornecedor in fornecedores:
  print(fornecedor["Nome"], "→ R$", fornecedor["Preço"])

resultado = encontrar_menor_preco(fornecedores)

print()
print("===== MELHOR COTAÇÃO =====")
print("Fornecedor:", resultado["Nome"])
print("Preço: R$", resultado["Preço"])