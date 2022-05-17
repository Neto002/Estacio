'''def calcula_notas(numero_notas):
    soma_notas = 0
    for i in range(numero_notas):
        nota = float(input("Digite a nota: "))
        soma_notas += nota
        if nota < 0 or nota > 10:
            print("Nota inválida")
            return
    media = soma_notas / numero_notas
    print("Média: ", media)
    if media >= 7:
        print("Aprovado")
    elif media <= 5:
        print("Reprovado")
    else:
        print("Recuperação")


quantidade_notas = int(input("Digite a quantidade de notas a serem lidas: "))
calcula_notas(quantidade_notas)'''

'''def calcula_media(numero_notas):
    soma_notas = 0
    for i in range(numero_notas):
        nota = float(input("Digite a nota: "))
        soma_notas += nota
        if nota < 0 or nota > 10:
            print("Nota inválida")
            return
    media = soma_notas / numero_notas
    print("Média: ", media)

quantidade_notas = int(input("Digite a quantidade de notas a serem lidas: "))
calcula_media(quantidade_notas)'''

'''def calcula_idade(nome, idade):
    print("Nome: ", nome)
    print("Idade: ", idade)
    if idade >= 17:
        print("Maior de idade")
    else:
        print("Menor de idade")
    print("Ano de nascimento: ", 2022 - idade)


nome = input("Digite o nome: ")
idade = int(input("Digite a idade que fará nesse ano: "))
calcula_idade(nome, idade)'''

'''from math import factorial


def fatoriais():
    for i in range(1, 11):
        print("Fatorial de {} = {}".format(i, factorial(i)))

fatoriais()'''

'''nao sei a 5 nem a 6'''

'''from math import sqrt

def pitagoras(cateto_adjascente, cateto_oposto):
    hipotenusa = sqrt(cateto_adjascente ** 2 + cateto_oposto ** 2)
    print("Hipotenusa: ", hipotenusa)

cateto_adjascente = float(input("Digite o cateto adjacente: "))
cateto_oposto = float(input("Digite o cateto oposto: "))
pitagoras(cateto_adjascente, cateto_oposto)'''

'''from math import log

def calcula_logaritmo(numero, base):
    logaritmo = log(numero, base)
    print("Logaritmo de {} em base {}: {}".format(numero, base, logaritmo))

numero = float(input("Digite um número: "))
base = float(input("Digite a base: "))
calcula_logaritmo(numero, base)'''

'''def calcula_potencias():
    for i in range(11):
        print("{} elevado a {} = {}".format(2, i, 2 ** i))
    for i in range(11):
        print("{} elevado a {} = {}".format(3, i, 3 ** i))

calcula_potencias()'''

'''def calcula_media_formatada(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print("Média: {:.2f}".format(media))

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
calcula_media_formatada(nota1, nota2, nota3)'''

'''def tabuada(numero):
    for i in range(1, 11):
        print("{} + {} = {}".format(numero, i, numero + i))
    for i in range(1, 11):
        print("{} x {} = {}".format(numero, i, numero * i))

numero = int(input("Digite um número: "))
tabuada(numero)'''