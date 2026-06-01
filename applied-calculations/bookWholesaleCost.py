# Calcula o custo total de atacado de livros considerando desconto de 35% e frete por exemplar.

copias = int(input("Informe a quantidade de copias que deseja comprar: "))

valor_livros = copias * 24.95
frete = ((copias - 1) * 0.75) + 3
desconto = valor_livros * 0.35

total = valor_livros - desconto + frete

print(f'O custo total da compra é de R$ {total:.2f}')                   
