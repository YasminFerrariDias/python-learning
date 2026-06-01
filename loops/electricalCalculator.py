# Calcula tensão, resistência ou corrente elétrica com base na Lei de Ohm (U = R * i).
print("************************************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("************************************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("************************************************")
escolha = int(input("Qual grandeza deseja calcular?"))

if escolha == 1:
    R = float(input("Informe o valor da resistência: "))
    i = float(input("Informe o valor da corrente: "))
    U = R * i    
    print(f"O valor da tensão é {U}")

elif escolha == 2:
    U = float(input("Informe o valor da tensão: "))
    i = float(input("Informe o valor da corrente: "))
    if i == 0:
        print("Corrente não pode ser 0")
    else:
        R = U/i        
        print(f"O valor da resistência é {R}")

elif escolha == 3:
    U = float(input("Informe o valor da tensão: "))
    R = float(input("Informe o valor da resistência: "))
    if R == 0:
        print("Resistencia não pode ser 0")
    else:
        i = U/R
        print(f"O valor da corrente é {i}")
else: 
    print("Insira um valor válido!")
