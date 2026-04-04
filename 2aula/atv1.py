# Escreva um Script em linguagem Python que receba 2 valores de x e y. Em seguida calcule e imprima o valor de z:

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

try:
    z = (x**2 + y**2)/(x-y)
    print(f'O resultado da conta é {z:.2f}')
except ZeroDivisionError:
    print("Não é possível realizar a conta com esse número, tente novamente.")

