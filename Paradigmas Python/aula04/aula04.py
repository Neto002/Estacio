#Ler 2 numeros e dizer qual é maior

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if (n1 > n2):
    print(f'O maior número entre eles é: {n1}')
elif (n1 < n2):
    print(f'O maior número entre eles é: {n2}')
else:
    print('Os números são iguais')