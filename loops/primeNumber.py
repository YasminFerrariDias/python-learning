# Verifica se um número inteiro informado é primo ou não.
import math

numero = int(input("Insira um número: "))

if numero <= 1:
    print(f"O número {numero} não é um número primo!")

else:
    primo = True
    limite = int(math.sqrt(numero))

    for i in range(2, limite + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"O número {numero} é um número primo!")
    else:
        print(f"O número {numero} não é um número primo!")
