# Lê dois conjuntos de 5 elementos, intercala e exibe as três listas.
lista1 = []
lista2 = []
tudo = []

for i in range(1, 6):
    lista1.append(int(input(f'Insira o {i}° elemento da lista 1: ')))

for i in range(1, 6):
    lista2.append(int(input(f'Insira o {i}° elemento da lista 2: ')))

for i in range(5):
    tudo.append(lista1[i])
    tudo.append(lista2[i])
                
print(lista1)
print(lista2)
print(tudo)
