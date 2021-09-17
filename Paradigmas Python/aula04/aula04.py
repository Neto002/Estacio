'''#Criando Métodos
def imprimir_Tela():
    print('Testando esse print')
imprimir_Tela()

#Método de cálculos
def soma(a, b):
    return a + b
print(soma(5, 1))

def calc_fatorial(numero):
    i = numero
    fatorial = 1
    for i in range(numero, 0, -1):
        fatorial *= i
    return fatorial

numero = int(input('Digite um número: '))
print(f'O valor do fatorial de {numero} é {calc_fatorial(numero)}')'''

#Exercicio 1
#Faça um programa q leia n notas de um aluno que estejam entre 0 e 10 e informe se o aluno está aprovado (>=7), reprovado (<=5) ou recuperação (>= 5,1 e <= 6,9)

def calcula_media():
    n = 0
    qtd = 0
    media = 0
    soma = 0
    while True:
        while True:
            n = float(input('Digite a nota: '))
            if (n >= 0 and n <= 10):
                break
            else:
                print('Por favor, digite um valor de 0 a 10.')
        soma += n
        qtd += 1
        resposta = ''
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper() [0]
        if (resposta in 'N'):
            break
    media = soma/qtd
    return media    

n = calcula_media()
if (n >= 7):
    print('APROVADO')
elif (n <= 5):
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')
print(f'Nota: {n:.2f}')

#Media aritmetica de n notas

print(f'A média aritmética é: {calcula_media():.2f}')

#Leia nome e idade e apresente se a pessoa é maior de idade (>=17) e em q ano nasceu

nome = str(input('Digite seu nome: ')).strip().title()
idade = int(input('Digite sua idade: '))
ano_nascimento = 2021 - idade

if (idade >= 17):
    print(f'Maior de idade, nasceu no ano {ano_nascimento}')
else:
    print(f'Menor de idade, nasceu no ano {ano_nascimento}')

#Um algoritmo em Python que calcule uma lista dos fatorial dos números de 1 até 10 e imprima.

#Solicita do usuário o número de elementos de um conjunto (𝑛) e o valor da combinação dos elementos desse conjunto (𝑘) e imprima a qtde de elementos resultantes da combinação,tal que 𝑛>=𝑘.

#Faça o mesmo exercício anterior para saber a quantidade de elementos resultantes da permutação.

#Solicita do usuário os valores do cateto e retorna a hipotenusa.

#Calcule o logaritmo de um número informado pelo usuário, juntamente com a sua base.