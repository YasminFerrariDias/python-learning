# Crie um Script em linguagem Python que peça um valor e imprima na tela se o valor
# é positivo, negativo ou ainda igual a zero.

number = int(input("Informe um número: "))

if number > 0:
    print("O número é positivo.")
elif number < 0:
    print("O número é negativo.")
elif number == 0:
    print("O número é igual a zero.")
else: 
    print("Insira um valor válido.")
