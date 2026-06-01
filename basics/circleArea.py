# Calcula a área de um círculo com base no raio informado usando pi = 3.14159.

comprimento = float(input('Informe um número de unidade de comprimento (um fracionário): '))

pi = 3.14159

if area_circulo >= 0:
    area_circulo = pi*comprimento**2
    print(f'A área do círculo de raio {comprimento} unidades é {area_circulo}')
else:
    print('Erro: valores negativos não são permitidos.')
