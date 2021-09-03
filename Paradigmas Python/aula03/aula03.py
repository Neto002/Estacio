#Exercício 1: informar se o numero informado é par ou ímpar

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
    print('Digite uma idade válida')

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

#Exercícios para a próxima aula

#Exercicio 1: pedir dois numeros e imprimir a sequencia entre eles

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n2 > n1:
    for c in range(n1, n2+1):
        print(c)
elif n2 < n1:
    for c in range(n2, n1, -1):
        print(c)
elif n2 == n1:
    print(n1)

#Exercicio 2: fatorial

num = int(input('Digite um numero: '))
c = num
f = 1

print(f'{num}! = ', end="")
for c in range(num, 0, -1):
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
print(f'{f}')

#Exercício 3: exibir a soma de todos os numeros entre 1 e 50

soma = 0
for c in range(1, 51):
    print(f'{c} ', end='')
    soma += c
print(f'\nA soma entre os números é: {soma}')