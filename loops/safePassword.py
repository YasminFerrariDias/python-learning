# Solicita a senha de um cofre em loop até que o valor correto seja inserido.
while True:
    senha = int(input("Digite a senha do cofre: "))

    if senha != 987654:
        print("Senha incorreta!")
    else: 
        print("Cofre aberto")
        break
