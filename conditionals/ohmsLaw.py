# Verifica se um componente elétrico obedece à Lei de Ohm com base em tensão, corrente e resistência.

V = float(input("Insira o valor da tensão em Volts:"))
I = float(input("Insira o valor da corrente em Amperes:"))
R = float(input("Insira o valor da resistência em Ohms:"))

valor = I * R

if V == valor:
    print("O componente obedece à Lei de Ohm.")
else: 
    print("O componente não obedece à Lei de Ohm.")
