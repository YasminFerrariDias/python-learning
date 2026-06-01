# Cadastra três produtos com nome e preço em um dicionário e os exibe ao final.
dicionario = {}

for i in range(1, 4):
    nome = input(f"Nome do {i}° produto: ")
    preco = int(input(f"Preço do {i}° produto: "))

    prod = []
    prod.append(preco)

    dicionario.update({nome: prod})

print("PRODUTOS")
for nome, prod in dicionario.items():
    print(f"{nome}: {prod}")
