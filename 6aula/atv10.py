# João precisa que você faça um script em linguagem Python que leia a variável peso (peso de peixes) e calcule o excesso.

peso = int(input('Informe o peso dos peixes: '))

excesso = peso - 50

if excesso <= 0:
    print(f'Você está dentro do limite, não terá multa')
elif excesso > 0:
    multa = excesso * 4
    print(f'Você pescou {excesso} quilos a mais.')
    print(f'Sua multa é de {multa}.')
