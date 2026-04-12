# Dados o valor da compra e o percentual de desconto, calcule o valor a ser pago. Considere que o percentual de desconto é um número real entre 0 e 1.

valor = float(input("Informe o valor da compra: "))
percentual = float(input("Informe o percentual  de desconto (entre 0 e 1, ex: 10% = 0.1): "))

desconto = valor * percentual
final = valor - desconto

print(f'O valor a ser pago é {final:.2f}')
