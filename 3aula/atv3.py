# Elabore um Script em linguagem Python que solicite o valor do investimento (PV), o número de meses (n) que irá permanecer aplicado e  a rentabilidade (i). Ao final, o script deve mostrar o valor do montante total (FV).

pv = float(input("Digite o valor do investimento: "))
n = int(input("Digite a quantidade de meses: "))
taxa = float(input("Digite a taxa de juros anuais: "))

i = taxa/12/100.0

fv = pv*(1+i)**n

print("O valor do montante é de ", fv)


