# Um novo modelo de carro, super econômico foi lançado. Ele faz 20 km com 1 litro de combustível. Cada litro de combustível custa R$ 4,95.

dinheiro = float(input("Qual a quantidade de dinheiro você pretende colocar de combustivel? "))

litro = dinheiro / 4.95
km = litro * 20
 
print("Você pode colocar: %.2f litros de combustível." % (litro))
print("Que vai rodar: %.2f quilômetros." % (km))
 
