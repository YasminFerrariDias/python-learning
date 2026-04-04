# Desenvolva um Script em linguagem Python que leia o número de litros vendidos e o tipo de combustível (codificado com A – Álcool e G – Gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo que o litro da gasolina está em R$ 5,57 e do álcool R$ 4,98.

litro = float(input("Informe a quantidade de litros vendido: "))
tipo = input("Informe o tipo de combustivel (A - alcool OU G - gasolina): ")

if tipo == "A":
    if litro <= 20:
        valor = round(litro * 4.98 * (1 - 2/100))
        print(f"ÁLCOOL - Você possue um desconto de 2%, o valor total é de {valor:.2f}")
    elif litro > 20:
        valor = round(litro * 4.98 * (1 - 5/100))
        print(f"ÁLCOOL - Você possue um desconto de 5%, o valor total é de {valor:.2f}")
    elif litro <= 0:
        print("Insira um valor válido!")

elif tipo == "G":
    if litro <= 20:
        valor = round(litro * 5.57 * (1 - 4/100))
        print(f"GASOLINA - Você possue um desconto de 4%, o valor total é de {valor:.2f}")
    elif litro > 20:
        valor = round(litro * 5.57 * (1 - 6/100))
        print(f"GASOLINA - Você possue um desconto de 6%, o valor total é de {valor:.2f}")
    elif litro <= 0:
        print("Insira um valor válido!")

else:
    print("Insira um tipo válido (A/G)")
