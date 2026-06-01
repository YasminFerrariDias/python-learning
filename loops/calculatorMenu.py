# Calculadora com menu de opções: adição, subtração, multiplicação, divisão e saída.
while True:
    numero1 = int(input("Digite o número 1: "))
    numero2 = int(input("Digite o número 2: "))

    escolha = int(input("Escolha uma opção: 1 - adição; 2 - subtração; 3 - multiplicação; 4 - divisão; 5 - saída;"))

    if escolha == 4 and numero2 == 0:
        print("Não é possível dividir por 0")
    else:
        if escolha == 1:
            resultado = numero1 + numero2
            print(f"O resultado é {resultado}")
        elif escolha == 2:
            resultado = numero1 - numero2
            print(f"O resultado é {resultado}")
        elif escolha == 3:
            resultado = numero1 * numero2
            print(f"O resultado é {resultado}")
        elif escolha == 4:
            resultado = numero1 / numero2
            print(f"O resultado é {resultado}")
        elif escolha == 5:
            print(f"Encerrado!")
            break
        else:
            print(f"Insira valores válidos")
