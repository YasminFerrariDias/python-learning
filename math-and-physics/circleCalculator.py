# Calcula a área e o perímetro de um círculo a partir do raio informado.
# Escreva um Script em linguagem Python que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo.

raio = float(input("Informe o raio de um círculo: "))

pi = 3.141592653589793

area = pi * raio**2
perimetro = 2 * pi * raio

print("ÁREA do círculo: %.2f" % (area))
print("PERIMETRO do círculo: %.2f" % (perimetro))
