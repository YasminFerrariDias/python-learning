# Lê 10 números e armazena apenas os não repetidos em uma lista.
numero = []

for i in range(1, 11):
    num = int(input(f"Digite o {i}° número positivo: "))
    
    if num not in numero:
        numero.append(num)
    else:
        continue

print(numero)
