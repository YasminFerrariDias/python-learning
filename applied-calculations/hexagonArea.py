# Calcula a área de um hexágono regular com base no raio informado.

import math

raio = float(input("Informe o raio do hexágono regular (em metros): "))

area = (3 * math.sqrt(3) * raio**2) / 2

print("A área do hexágono é de %.2f" % (area))
