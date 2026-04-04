# Neste exercício, você irá criar um Script em linguagem Python que verifica se um componente elétrico está obedecendo à Lei de Ohm. A Lei de Ohm relaciona a tensão (V), a corrente (I) e a resistência (R) de um componente elétrico através da fórmula V = I * R

V = float(input("Insira o valor da tensão em Volts:"))
I = float(input("Insira o valor da corrente em Amperes:"))
R = float(input("Insira o valor da resistência em Ohms:"))

valor = I * R

if V == valor:
    print("O componente obedece à Lei de Ohm.")
else: 
    print("O componente não obedece à Lei de Ohm.")
