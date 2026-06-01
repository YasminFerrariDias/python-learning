# Lê dois conjuntos de três valores e exibe uma lista com a soma dos elementos correspondentes.
lista1 = []
lista2 = []
lista_resultante = []

for i in range(1, 4):
    item = int(input(f"Digite o {i}° valor da 1° lista: "))
    lista1.append(item)

for i in range(1, 4):
    item = int(input(f"Digite o {i}° valor da 2° lista: "))
    lista2.append(item)

for i in range(3):
    item_lista = lista1[i] + lista2[i]
    lista_resultante.append(item_lista)

print(lista_resultante)
