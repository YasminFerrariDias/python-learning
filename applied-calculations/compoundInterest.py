# Calcula o montante final (FV) de um investimento com base no valor inicial, meses e taxa de juros anual.

pv = float(input("Digite o valor do investimento: "))
n = int(input("Digite a quantidade de meses: "))
taxa = float(input("Digite a taxa de juros anuais: "))

i = taxa/12/100.0

fv = pv*(1+i)**n

print("O valor do montante é de ", fv)


