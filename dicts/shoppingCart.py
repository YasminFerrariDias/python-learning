# Cadastra produtos com código, nome, preço e quantidade em loop e exibe o total da compra.
produtos = {}

while True:
    cod = input("Código: ")
    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade comprada: "))

    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(quantidade)
    produtos.update({cod: prod})
    
    sair = input("Sair (S/N)? ")
    if sair == "N" or sair == "n":
        continue
    elif sair == "S" or sair == "s":
        break
    else: 
        print("Insira valores válidos.")

total = 0

for cod, prod in produtos.items():
    subtotal = produtos[cod][1] * produtos[cod][2]
    print(f"{prod[0]} - R$ {subtotal:.2f}")
    total += subtotal

print(20 * "-")
print(f"Total: R$ {total:.2f}")
