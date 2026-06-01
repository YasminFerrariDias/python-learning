# Calcula a área de uma coroa circular com base nos raios maior e menor informados.

import math

raio_maior = float(input("Informe o raio maior: "))
raio_menor = float(input("Informe o raio menor: "))

area_maior = math.pi * raio_maior**2
area_menor = math.pi * raio_menor**2

coroa = area_maior - area_menor

print("A medida da coroa circular é de %.2f" % (coroa))
