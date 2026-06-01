# Lê a temperatura média de cada mês e exibe os meses com temperatura acima da média anual.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dic = {}
soma = 0

for i in range(12):
    temperatura = float(input(f"Digite a média de temperatura de {meses[i]} (C°): "))

    dados = []
    dados.append(meses[i])
    dados.append(temperatura)
    dic.update({i + 1: dados})
    soma += temperatura

media = soma/12

print("MESES ACIMA DA MÉDIA ANUAL:")
print(f"Média anual: {media}")
for cod, dados in dic.items():
    if dados[1] > media:
        print(f"{[cod]} - {dados[0]}")
