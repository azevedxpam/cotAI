from cotacao import encontrar_menor_preco

def apresentar():
  print("Olá, eu sou o CotAI!")

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

def ler_quantidade():
  while True:
    try: 
      quantidade = int(input("Qual a quantidade? "))
      if quantidade > 0:
        return quantidade
      print("A quantidade deve ser maior que 0.")

    except ValueError:
      print("Quantidade inválida.")

def cadastrar_pedido():
  produto = input("Qual produto você deseja cotar? ")
  quantidade = ler_quantidade()

  pedido = {
    "Produto" : produto,
    "Quantidade" : quantidade
  }

  return pedido

apresentar()
pedido = cadastrar_pedido()
fornecedores = cadastrar_fornecedores()
print()

for fornecedor in fornecedores:
  print(fornecedor["Nome"], "→ R$", fornecedor["Preço"])

resultado = encontrar_menor_preco(fornecedores)

print()
print("===== COTAÇÃO =====")
print("Produto:", pedido["Produto"])
print("Quantidade:", pedido["Quantidade"])
print()
print("===== MELHOR COTAÇÃO =====")
if len(resultado) == 1:
  print("Fornecedor:", resultado[0]["Nome"])
  print("Preço: R$", resultado[0]["Preço"])
else:
  print("Empate entre os fornecedores:")
  for fornecedor in resultado :
    print(fornecedor["Nome"],"→ R$",fornecedor["Preço"])
print()