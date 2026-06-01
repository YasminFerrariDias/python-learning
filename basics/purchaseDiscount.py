# Calcula o valor final de uma compra aplicando um percentual de desconto entre 0 e 1.

valor = float(input("Informe o valor da compra: "))
percentual = float(input("Informe o percentual  de desconto (entre 0 e 1, ex: 10% = 0.1): "))

desconto = valor * percentual
final = valor - desconto

print(f'O valor a ser pago é {final:.2f}')
