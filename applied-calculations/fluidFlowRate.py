# Calcula a vazão de um fluido em um tubo com base no diâmetro interno e na velocidade do fluxo.

import math

diametro = float(input("Informe o diâmetro interno do tubo: "))
velocidade = float(input("Informe a velocidade do fluxo: "))

vazao = (math.pi * diametro**2) / 4 * velocidade

print("A vazão é de %.2f" % (vazao))
