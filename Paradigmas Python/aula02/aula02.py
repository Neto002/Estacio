'''1) Elabore os seguintes programas em Python:

   a) Solicite dois numeros inteiros do usuario e imprima:

    i. a soma, subtração e a multiplicação
    ii. o resto da divisão dos dois numeros

   b) Solicite o nome e o ano de nascimento do usuário e informe a sua idade
    
   c) Solicite tres notas do usuario e calcule a media final'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print(f'A soma entre os dois é {numero1 + numero2}\nSubtração: {numero1 - numero2}\nMultiplicação: {numero1 * numero2}\nResto da divisão: {numero1 % numero2}')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2021

nome = str(input('Digite seu nome: ')).title().strip()

print(f'{nome}, você tem {ano_atual-ano_nascimento} anos.')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
nota3 = float(input('Digite sua nota 3: '))

print(f'Sua média final é: {(nota1+nota2+nota3)/3}')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------