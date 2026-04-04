# Você foi contratado para desenvolver um Script em linguagem Python que calcule o Índice de Massa Corporal (IMC) com base nos dados de altura e peso fornecidos pelo usuário. O IMC é uma medida que relaciona o peso e a altura de uma pessoa para avaliar se ela está abaixo do peso, com peso normal, com sobrepeso ou obesa. A fórmula para calcular o IMC é: IMC = peso / (altura^2), onde o peso é em quilogramas e a altura é em metros.

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
