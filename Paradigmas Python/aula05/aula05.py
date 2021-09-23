'''def func():
    x = 1
    print(x)
    return x

valor_x = func()
print("O valor de x é: ", valor_x)

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

print(listsum([2,4,5,6,3,]))

nota = float(str(input('numero: ').replace(',', '.')))

print(nota)'''


# Elabore um programa que imprima uma sequência da tabuada da potência de base 2 e base 3 de uma lista de 0 até 10.

for i in range (0, 11):
    print(f'2^{str(i).} = {pow(2, i)}', end=', ' if i < 10 else '.')
print()
for i in range (0, 11):
    print(f'3^{i} = {pow(3, i)}', end=', 'if i < 10 else '.')
print()

# Faça um algoritmo em python q leia 3 notas e faça a media, formatada com duas casas decimais

notas = [float(input('Digite a primeira nota: ')), float(input('Digite a segunda nota: ')), float(input('Digite a terceira nota: '))]
print(f'A média entre as três notas é: {(notas[0] + notas[1] + notas[2])/3:.2f}')

# Imprimir tabuada de soma e multiplicação de um numero informado

numero = int(input('Digite um numero: '))

print('Soma:')
for i in range(1, 11):
    print(f'{numero} + {i} = {numero + i}')
print('Multiplicação:')
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')