# Calcula soma, quantidade, média, variância e desvio padrão de uma tupla de vendas mensais.
import math

soma = 0
quantidade = 0

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

for i in Vendas:
    soma += i
    quantidade += 1

media = soma/quantidade
variancia = (soma - media)**2/quantidade
desvio_padrao = math.sqrt(variancia)

print(soma)
print(quantidade)
print(media)
print(variancia)
print(desvio_padrao)
