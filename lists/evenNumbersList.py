# Lê números positivos em loop e armazena apenas os pares, encerrando ao digitar 0.
L = []

while True:
    numero = int(input("Digite um número positivo (para sair, digite 0): "))

    if numero == 0:
        print(L)
        break
    elif numero % 2 == 0:
        L.append(numero)
    else:
        continue
