# Leia 2 strings e informe o conteúdo delas mais seu comprimento e informe tbm se as duas possuem o mesmo comprimento

'''str1 = str(input('Digite a primeira string: '))
str2 = str(input('Digite a segunda string: '))

print(f'String 1: \nConteúdo: {str1}\nComprimento: {len(str1)}')
print(f'String 2: \nConteúdo: {str2}\nComprimento: {len(str2)}')

if (len(str1) == len(str2)):
    print('As duas strings têm o mesmo comprimento')
elif (len(str1) > len(str2)):
    print('A string 1 é maior')
elif (len(str2) > len(str1)):
    print('A string 2 é maior')'''

# Leia o nome de uma pessoa e imprima da seguinte forma e com letras maiusculas

'''nome = str(input('Digite aqui seu nome: ')).strip().upper()

for i in nome:
    print(i)'''

# Leia um numero de celular e corrija-o no caso deste conter somente 8 digitos, acrescentando 9 na frente. Valide se o usuario esta de fato digitando apenas numeros de 9 ou 10 qtde. Ex: Se o nmr informado for 92902365, conserte adicionando um 9 na frente; Se digitou 9992902365 então é invalido

'''numero = str(input('Digite seu número de celular: ')).strip()

if (numero.isnumeric() == False):
    print('Por favor, digite somente números.')
elif (len(numero) == 8):
    numero = '9' + numero
    print(f'O número devidamente formatado é {numero[0:5]} {numero[5:]}')
elif (len(numero) > 9 or len(numero) < 8):
    print('O número está inválido')
else:
    print(f'O número informado foi: {numero[0:5]} {numero[5:]}')'''