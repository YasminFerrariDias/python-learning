# Você está desenvolvendo um Script em linguagem Python para calcular a vazão de um fluido em um tubo com base no diâmetro interno do tubo e na velocidade do fluxo. A fórmula para calcular a vazão deve ser pesquisada. Os dados de entrada devem ser alimentados em metros e m/s.

import math

diametro = float(input("Informe o diâmetro interno do tubo: "))
velocidade = float(input("Informe a velocidade do fluxo: "))

vazao = (math.pi * diametro**2) / 4 * velocidade

print("A vazão é de %.2f" % (vazao))
