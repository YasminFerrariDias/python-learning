# Lê duas notas de 5 alunos, calcula a média de cada um e exibe quantos obtiveram média igual ou acima de 7.
soma_nota = 0
tudo = []
novo = []

for aluno in range(1, 6):
    for nota in range(1, 3):
        notas = float(input(f"Insira a {nota}° nota do {aluno}° aluno: "))
        soma_nota += notas

    media = soma_nota/2
    soma_nota = 0
    tudo.append(media)

for i in tudo:
    if i >= 7:
        novo.append(i)

print(f"A quantidade de alunos a tirar nota acima ou igual à 7 foi {len(tudo)} alunos, as médias foram: {novo}")
