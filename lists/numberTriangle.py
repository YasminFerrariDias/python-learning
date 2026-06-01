# Exibe um triângulo numérico sequencial com N linhas informadas pelo usuário.
n = input("Digite a quantidade de linhas: ")
numero = 1

if n.isdigit():
    n = int(n)
    for linhas in range(1, n + 1):
        for quant in range(1, linhas + 1):
            print(numero, end=" ")
            numero += 1
        print()
else:
    print("Valor inválido!")
