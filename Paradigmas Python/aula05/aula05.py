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
'''frase = 'testeformat'
print(f'{frase:>20}')
print(f'{frase:#>20}')
print(f'{frase:#^20}')
print(f'{frase:.6}')'''

# Faça um programa em Python que tendo dois números inteiros informados do teclado, imprima a soma, multiplicação, subtração e divisão entre esses dois números. O programa deve impedir o usuário de informar o número zero no denominador da divisão.

'''while True:
    num1 = float(input('Digite o primeiro número: '))
    while (num1 == 0):
        num1 = float(input('Digite um número diferente de 0: '))
    num2 = float(input('Digite o segundo número: '))
    while (num2 == 0):
        num2 = float(input('Digite um número diferente de 0: '))
    if (num1 != 0 or num2 != 0):
        break
print(f'Soma: {num1+num2}\nMultiplicação: {num1*num2}\nSubtração: {num1-num2}\nDivisão: {num1/num2}')'''

# Faça um algoritmo em Python que imprima na tela os números de 1 a 100 que são múltiplos de 4, um abaixo do outro. O mesmo programa também deve imprimir esses números um ao lado do outro. Imprima também a quantidade desses números.

'''qtd = 0
for i in range(1, 101):
    if (i % 4 == 0):
        print(i)
        qtd += 1
print(f'A quantidade de múltiplos de 4 é {qtd}')

qtd = 0
for i in range(1, 101):
    if (i % 4 == 0):
        print(i, end=', ' if i < 100 else '.\n')
        qtd += 1
print(f'A quantidade de múltiplos de 4 é {qtd}')'''
