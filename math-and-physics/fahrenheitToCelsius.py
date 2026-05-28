# Converte temperatura de Fahrenheit para Celsius.
# Agora faça o contrário. Você fornece a temperatura em graus Fahrenheit, seu Script converte para Celsius e exibe na tela.

fahrenheit = float(input("Informe a temperatura: "))

celsius = (fahrenheit - 32)/1.8
 
print("A temperatura em Celsius: %.2f" % (celsius))
