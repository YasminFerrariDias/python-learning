# Cadastra funcionários e impede demissão de programadores com 3 ou mais anos de serviço.
func = {}

for i in range(1, 3):
    cod = int(input("Índice numerico: "))
    nome = input("Nome: ")
    funcao = input("Função: ")
    tempo = int(input("Tempo de serviço (anos): "))

    dados = []
    dados.append(nome)
    dados.append(funcao)
    dados.append(tempo)
    func.update({cod: dados})

print(f"FUNCIONARIOS: {func}")
remover = int(input("Escolha um funcionário com base no seu índice numerico para ser demitido: "))

try:
    for cod, dados in func.items():
        if func[cod][1] == "Programador" and func[cod][2] >= 3:
            print("Não é possível demiti-lo")
            break
        else:
            func.pop(remover)
            print("Demitito com sucesso!")
except KeyError:
    print("Índice inválido")

print(f"FUNCIONARIOS: {func}")
