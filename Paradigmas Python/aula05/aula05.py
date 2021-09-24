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


'''# Elabore um programa que imprima uma sequência da tabuada da potência de base 2 e base 3 de uma lista de 0 até 10.

for i in range (0, 22):
    if (i <= 10):
        print(f'2^{i} = {pow(2, i)}', end=', ' if i < 10 else '.\n') 
    else:
        print(f'3^{i-11} = {pow(3, i-11)}', end=', 'if i < 21 else '.\n')

# Faça um algoritmo em python q leia 3 notas e faça a media, formatada com duas casas decimais

notas = [float(input('Digite a primeira nota: ')), float(input('Digite a segunda nota: ')), float(input('Digite a terceira nota: '))]
print(f'A média entre as três notas é: {(notas[0] + notas[1] + notas[2])/3:.2f}')

# Imprimir tabuada de soma e multiplicação de um numero informado

numero = int(input('Digite um numero: '))

for i in range(1, 21):
    if (i <= 10):
        if(i == 1):
            print('Soma:')
        print(f'{numero} + {i} = {numero + i}')
    else:
        if(i == 11):
            print('Multiplicação:')
        print(f'{numero} x {i-10} = {numero * (i-10)}')'''


# Comandos de formatação
frase = 'testeformat'
print(f'{frase:>20}')
print(f'{frase:#>20}')
print(f'{frase:#^20}')
print(f'{frase:.6}')