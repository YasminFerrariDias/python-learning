# Elabore um script em linguagem Python que determine se um ano introduzido pelo usuário é ou não bissexto. Um ano é bissexto se for múltiplo de 4 sem ser de 100 ou se for múltiplo de 400. 

ano = int(input('Informe um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é um ano bisexto.')
else:
    print(f'O ano {ano} não é um ano bisexto.')

