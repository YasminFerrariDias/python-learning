# Calcula o valor total de um produto com base no valor unitário, quantidade e desconto informados.
valorUnitario = float(input("Informe o valor unitário do produto: "))
quantidade = int(input("Informe a quantidade: "))
desconto = float(input("Informe o valor do desconto: "))
valorTotal = (valorUnitario * quantidade) - desconto

print("O valor total é R$", valorTotal)