# Calcula o IMC com base em peso e altura e classifica o resultado em categorias.

altura = float(input("Informe sua altura (metros): "))
peso = float(input("Informe seu peso (kg): "))

imc = peso / altura**2

if imc < 18.5:
    print("Abaixo do peso — IMC: %.2f" % imc)
elif 18.5 <= imc <= 24.9:
    print("Peso normal — IMC: %.2f" % imc)
elif 25 <= imc <= 29.9:
    print("Sobrepeso — IMC: %.2f" % imc)
elif 30 <= imc <= 34.9:
    print("Obesidade grau I — IMC: %.2f" % imc)
elif 35 <= imc <= 39.9:
    print("Obesidade grau II (severa) — IMC: %.2f" % imc)
else:
    print("Obesidade grau III (mórbida) — IMC: %.2f" % imc)
