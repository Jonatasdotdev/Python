# Catálogo de produtos
catalogo = {
  "100": {
    "especificacao": "Calça",
    "preco": 200.0
  },
  "200": {
    "especificacao": "Bermuda",
    "preco": 100.0
  },
  "300": {
    "especificacao": "Camiseta",
    "preco": 75.0
  },
  "400": {
    "especificacao": "Calça Jeans",
    "preco": 185.0
  },
  "500": {
    "especificacao": "Camisa Regata",
    "preco": 65.0
  },
  "600": {
    "especificacao": "Biquini",
    "preco": 89.0
  }
}

# Variáveis para controlar o pedido e o total a pagar
pedido_encerrado = False
total_a_pagar = 0.0

# Loop principal do programa
while not pedido_encerrado:
  # Leitura do código do item e da quantidade desejada
  codigo = input(
    "Digite o código do item desejado (ou 'fim' para encerrar o pedido): ")
  if codigo.lower() == "fim":
    pedido_encerrado = True
  else:
    quantidade = int(input("Digite a quantidade desejada: "))

    # Cálculo do valor a pagar por item e atualização do total a pagar
    item = catalogo.get(codigo)
    if item:
      preco_unitario = item["preco"]
      valor_a_pagar = preco_unitario * quantidade
      total_a_pagar += valor_a_pagar
      print(
        f"Item: {item['especificacao']} | Preço unitário: R$ {preco_unitario:.2f} | Quantidade: {quantidade} | Valor a pagar: R$ {valor_a_pagar:.2f}"
      )
    else:
      print("Código inválido. Tente novamente.")

# Exibição do total a pagar
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
