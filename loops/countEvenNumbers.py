# Lê 5 números inteiros positivos e conta quantos são pares.
par = 0

for i in range(5):
    numero = int(input("Insira um número: "))
    if numero % 2 == 0:
        par += 1

print(f"Foi digitado {par} números pares")
