# Lê quatro notas de 10 alunos, calcula a média de cada um e conta quantos obtiveram média igual ou superior a 7.
i = 1
lista = []
soma = 0
for i in range(1, 11):
    soma = 0
    
    for n in range(1,5):
        nota = int(input(f'Insira a {n}° nota do aluno {i}°: '))     

        if nota > 10 or nota < 0:
            print('Insira valores válidos')

        else:
            soma += nota 
            if soma > 0:
                media = soma/4
                lista.append(media)
            
            elif soma == 0:
                lista.append(soma)
            
            else:
                print('Insira valores válidos')    
            continue

i = 0
alunos = 0
while i < len(lista):
    if lista[i] >= 7:
        alunos += 1
    i += 1
        
print(f'{alunos} alunos conseguiram com a média igual ou superior a 7')
