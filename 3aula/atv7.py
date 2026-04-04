# Você foi contratado para desenvolver um Script em linguagem Python que calcule área de uma coroa circular com base em duas medidas de raio fornecido pelo usuário.

import math

raio_maior = float(input("Informe o raio maior: "))
raio_menor = float(input("Informe o raio menor: "))

area_maior = math.pi * raio_maior**2
area_menor = math.pi * raio_menor**2

coroa = area_maior - area_menor

print("A medida da coroa circular é de %.2f" % (coroa))
