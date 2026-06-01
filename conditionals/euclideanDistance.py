# Calcula a distância euclidiana entre dois pontos P1 e P2 no plano cartesiano.
import math

x1 = int(input("Defina o x1: "))
y1 = int(input("Defina o y1: "))
x2 = int(input("Defina o x2: "))
y2 = int(input("Defina o y2: "))

d = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

print("A distância entre P1({}, {}) e P2({}, {})".format(x1, y1, x2, y2))
