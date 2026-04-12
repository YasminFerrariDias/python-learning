# Escreva um script em linguagem Python para ler um número de unidade de comprimento (um fracionário) e mostre a área do círculo deste raio. Assuma com valor do pi 3.14159 (uma apropriada declaração deve ser dada a esta constante). A saída deveria ter a seguinte forma:

comprimento = float(input('Informe um número de unidade de comprimento (um fracionário): '))

pi = 3.14159

if area_circulo >= 0:
    area_circulo = pi*comprimento**2
    print(f'A área do círculo de raio {comprimento} unidades é {area_circulo}')
else:
    print('Erro: valores negativos não são permitidos.')
