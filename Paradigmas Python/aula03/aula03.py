'''#Exercício 1: informar se o numero informado é par ou ímpar

num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')

#Exercício 2: imprimir os numeros impares de 10 a 200 usando as duas estruturas de repetição

print('Utilizando o For')
for n in range(10, 201):
    if n % 2 != 0:
        print(f'{n} ', end='')

print('\nUtilizando o While')
n = 10
while n <= 200:
    if n % 2 != 0:
        print(f'{n} ', end='')
    n += 1

#Exercício 3: ler nome e idade de uma pessoa, imprima o nome e diga se a mesma é maior de idade

nome = str(input('Digite seu nome: ')).title().strip()
idade = int(input('Digite sua idade: '))

print(f'Nome: {nome}')
if idade >= 18:
    print(f'Idade: {idade} (MAIOR DE IDADE)')
elif idade < 18:
    print(f'Idade: {idade} (MENOR DE IDADE)')
else:
    print('Digite uma idade válida')'''

#Exercício 4 e 5: ler 3 numeros inteiros e dizer qual o maior e imprimi-los em ordem crescente

maior = 0
for c in range(3):
    num = int(input('Digite um numero: '))

    if c == 0:
        menor = num
        meio = num
        maior = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num
    
    if num > menor and num < maior:
        meio = num
print(f'O maior número digitado foi {maior}')
print(f'Imprimindo os três em ordem crescente: {menor}, {meio}, {maior}')