# Lê notas de duas provas de uma turma e compara as médias para determinar qual foi melhor.
P1 = []
P2 = []
soma1 = 0
soma2 = 0

limite = int(input("Tamanho da turma: "))

for i in range(limite):
    numero = float(input("Digite a nota da prova 1: "))
    if numero <= 10 or numero >= 0:
        P1.append(numero)
    else:
        print("Insira valores válidos!")

for i in range(limite):
    numero = float(input("Digite a nota da prova 2: "))
    if numero <= 10 or numero >= 0:
        P2.append(numero)
    else:
        print("Insira valores válidos!")

for i in P1:
    soma1 += i
media1 = soma1/len(P1)

for i in P2:
    soma2 += i
media2 = soma2/len(P2)

print(f"Média da prova 1: {media1:.2f}")
print(f"Média da prova 2: {media2:.2f}")

if media1 > media2:
    print(f"A turma obteve a melhor média na prova 1")
elif media1 < media2:
    print(f"A turma obteve a melhor média na prova 2")
else:
    print(f"A turma obteve o mesmo desempenho nas duas provas")
