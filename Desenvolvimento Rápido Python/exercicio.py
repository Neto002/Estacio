import datetime

# 1. Elabore um programa em Python que insere a tabuada de multiplicação de 9
# em um arquivo txt.

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/tabuada.txt", 'w+', encoding='utf-8') as file:
    for i in range(1, 11):
        file.write(f"9x{i} = {i*9}\n")

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/tabuada.txt", 'r+', encoding='utf-8') as file:
    print(file.read())

# 2. Faça um programa que leia os dados de uma pessoa (Nome, RG, CPF, ano de
# nascimento e armazene em um arquivo txt, calculando a idade da pessoa.

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/cpf.txt", 'w+', encoding='utf-8') as file:
    lista = [input('Digite seu nome: ').strip().title(), input('Digite seu RG: '),
             input('Digite seu CPF: '), input('Digite o ano em que você nasceu: ')]
    
    for i in lista:
        file.write(f"{i}\n")
    
    idade = datetime.datetime.today().year - int(lista[3])

    file.write(f"Você tem {idade} anos.\n")

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/cpf.txt", 'r+', encoding='utf-8') as file:
    print(file.read())

# 3. Faça um programa que leia um arquivo txt e insere cada linha em uma lista.

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/string.txt", 'r+', encoding='utf-8') as file:
    for line in file:
        print(line.split())


# 4. Elabore um programa em Python que leia o nome e duas notas de um aluno
# do teclado, calcule a média e armazene em um arquivo txt o nome, a média
# final e se o mesmo foi Aprovado (média >=6) ou Reprovado (média < 6).

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/media.txt", 'w+', encoding='utf-8') as file:
    dados = [input("Digite seu nome: ").strip().title(), input("Digite a primeira nota: ").strip(), input("Digite a segunda nota: ").strip()]

    media = (float(dados[1]) + float(dados[2]))/2

    situacao = 'APROVADO' if media >= 6 else 'REPROVADO'

    file.write(f"Nome: {dados[0]}\tMédia: {media:.2f}\tSituação: {situacao}")

# 5. Faça um algoritmo em Python que leia dois números inteiros do teclado, faça
# uma mini calculadora (soma, subtração, multiplicação e divisão) e armazene
# todos os resultados em um arquivo txt.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/calculadora.txt", 'w+', encoding='utf-8') as file:
    file.write(f"Soma: {n1+n2}\nSubtração: {n1-n2}\nMultiplicação: {n1*n2}\nDivisão: {n1/n2}")