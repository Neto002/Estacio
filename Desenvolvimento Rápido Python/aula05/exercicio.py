print("Defina o que é a metodologia RAD e suas principais fases. Descreva a importância dessa metodologia com o uso da linguagem de programação Python")

print("Faça um script que leia um nome completo direto de um arquivo txt e imprima na tela.")

'''with open("C:/Users/202102570735/Documents/GitHub/Estacio/Desenvolvimento Rápido Python/aula05/texto.txt", "w+") as file:
    file.write(input("Digite seu nome completo: ").strip().title())

with open("C:/Users/202102570735/Documents/GitHub/Estacio/Desenvolvimento Rápido Python/aula05/texto.txt", "r+") as file:
    print(file.read())'''

print("Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte")
print("Quantos espaços em branco existem na frase.")

'''frase = input("Digite aqui a frase: ").strip().capitalize()
print(f'Quantidade de espaços em branco na frase: {frase.count(" ")}')

print("Quantas vezes aparecem as vogais a, e, i, o, u.")
print(f'Quantidade de vogais: {frase.lower().count("a")} a, {frase.lower().count("e")} e, {frase.lower().count("i")} i, {frase.lower().count("o")} o, {frase.lower().count("u")} u.')'''

'''print("Faça um programa que leia uma sequência de caracteres, mostre-a e diga se é um palíndromo ou não")
string = input("Digite a palavra ou frase: ").strip().replace(" ", "").lower()
if string == string[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")'''

print("Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador")

'''telefone = input("Digite o telefone: ").strip()
# telefone = telefone.replace(telefone[telefone.find('-')], "")
if (telefone.find("-") == -1 and len(telefone) == 7 or telefone.find("-") != 0 and len(telefone) == 8):
    telefone = '3' + telefone
print(telefone)'''