# Verifica se um número é positivo, negativo ou igual a zero.

number = int(input("Informe um número: "))

if number > 0:
    print("O número é positivo.")
elif number < 0:
    print("O número é negativo.")
elif number == 0:
    print("O número é igual a zero.")
else: 
    print("Insira um valor válido.")
