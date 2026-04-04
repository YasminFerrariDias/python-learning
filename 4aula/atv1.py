# Crie um script em linguagem Python que exiba na tela o texto 'A melhor banda do mundo é [nome da banda] e a melhor música é [nome da música]'.O nome da banda e o nome da música devem estar declarados em duas variáveis diferentes

banda = input("Informe sua banda favorita: ")
musica = input("Qual a melhor música dela? ")

print("A melhor banda é a", banda, "com a música", musica)
print("A melhor banda é a %s com a música %s" % (banda, musica))
