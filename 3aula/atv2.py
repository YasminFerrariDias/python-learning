# Você está desenvolvendo um Script em linguagem Python para calcular a área de um hexágono regular com base no raio fornecido pelo usuário. Um hexágono regular tem seis lados de igual comprimento e seis ângulos internos de 120 graus. Assim, para determinar a área desse hexágono, basta determinar a área de um dos triângulos e, em seguida, multiplicar o resultado por 6.

import math

raio = float(input("Informe o raio do hexágono regular (em metros): "))

area = (3 * math.sqrt(3) * raio**2) / 2

print("A área do hexágono é de %.2f" % (area))
