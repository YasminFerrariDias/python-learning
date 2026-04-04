# Você está no Brasil, e para temperatura usamos o grau Celsius. Porém, quando você for contrato para trabalhar como programador Python no exterior, deverá usar graus Fahrenheit. Ou seja, você fornece a temperatura em graus Celsius, e seu Script faz a conversão para graus Fahrenheit.


celsius = float(input("Informe a temperatura: "))

fahrenheit = (celsius*1.8)+32
 
print("A temperatura em Fahrenheit: %.2f" % (fahrenheit))
