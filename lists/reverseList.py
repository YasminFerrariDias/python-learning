# Lê 10 números inteiros, armazena em lista e os exibe na ordem inversa.
lista = []

for i in range(1, 11):
    numero = int(input(f"Insira o {i}° número: "))
    lista.append(numero)

print(lista[::-1])
