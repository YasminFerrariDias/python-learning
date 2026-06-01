# Lê dois conjuntos de 6 valores e exibe a soma dos elementos correspondentes.
lista1 = []
lista2 = []
lista_resultante = []

for i in range(1, 7):
    numero = int(input(f"Insira o {i}° valor da lista 1: "))
    lista1.append(numero)

for i in range(1, 7):
    numero = int(input(f"Insira o {i}° valor da lista 2: "))
    lista2.append(numero)

for i in range(1, 6):
    lista_resultante.append(lista1[i] + lista2[i])

print(lista_resultante)
