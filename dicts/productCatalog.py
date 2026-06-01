# Cadastra produtos com código, nome, preço unitário e quantidade em um dicionário, exibindo o subtotal e total ao final.
produtos = {}

while True:
    cod = int(input("Código: "))
    nome = input("Nome do produto: ")
    preco_uni = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade: "))

    prod = []
    prod.append(nome)
    prod.append(preco_uni)
    prod.append(quantidade)
    produtos.update({cod: prod})

    resposta = input("Deseja continuar (S/N)? ")

    if resposta == "N" or resposta == "n":
        break
    elif resposta == "S" or resposta == "s":
        continue
    else: 
        print("Resposta inválida")

total = 0

for cod, prod in produtos.items():
    subtotal = produtos[cod][1] * produtos[cod][2]
    print(f'{prod[0]}: R$ {subtotal:.2f}')
    total += subtotal

print(20 * '-')
print(f"Total R$ {total:.2f}")
