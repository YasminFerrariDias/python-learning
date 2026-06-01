# Gera e exibe uma lista com todos os inteiros entre dois valores informados.
lista = []

x = int(input("Insira um valor inteiro para X: "))
y = int(input("Insira um valor inteiro para Y: "))

for i in range(x, y + 1):
    lista.append(i)

print(lista)
