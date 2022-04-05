# 1 - Faça um script que leia um nome e verifique se o nome é string válido, usando o try/except.

while True:
    try:
        nome = input('Digite seu nome: ').strip().title()
        if not nome.isalpha() or nome == '':
            raise ValueError('Nome inválido!')
        else:
            print(f'O nome {nome} é válido.')
            break
    except ValueError as e:
        print(f'Erro: {e}')


# 2 - Leitura de dois números inteiros do teclado e realizar a divisão dos números, fazendo os seguintes tratamentos das exceções caso exista divisão por zero ou um dos números digitados não sejam números.

while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        divisao = n1/n2
    except ZeroDivisionError:
        print('O segundo número deve ser diferente de 0.')
    except ValueError:
        print('Informe somente números.')
    else:
        print(f'A divisão entre os dois números é: {divisao}')
        break

# 3 - Tendo uma lista de números inteiros, faça o cálculo do fatorial de cada número da lista. Faça os seguintes tratamentos de exceções, caso exista um elemento da lista que não seja um número ou exista um número negativo.

import math

while True:
    try:
        lista = [int(x) for x in input("Digite uma lista de números inteiros (separe-os por espaço em branco): ").split()]
        for i in lista:
            if i < 0:
                raise ValueError()
            fatorial = math.factorial(i)
            print(f'Fatorial de {i}: {fatorial}')
    except ValueError:
        print("Por favor, digite somente números inteiros e positivos.")
    else:
        break

# 4 - Tendo um arquivo de texto, conte quantas palavras tem esse arquivo, além de contar quantas linhas existem. Seu script deve verificar se o arquivo está no diretório.

try:
    with open(r'D:\Projects\Estacio\Desenvolvimento Rápido Python\aula07\texto.txt', 'r+') as file:
        texto_arquivo = file.read()
        palavras = len(texto_arquivo.split())
        qtd_linhas = len(texto_arquivo.split('\n'))
        print(palavras)
except FileNotFoundError:
    print('Arquivo inexistente.')
except PermissionError:
    print("Sem permissão de acesso.")

# 5 - Um script que leia um nome completo, converta a primeira letra em letra maiúscula (joão silva => João Silva) e armazene dentro de um arquivo. Elabore tratamento de exceção para verificar se é um nome válido e se o arquivo está no diretório.

while True:
    try:
        nome = input('Digite seu nome: ').strip().title()
        if not nome.isalpha() or nome == '':
            raise ValueError('Nome inválido!')
        else:
            print(f'O nome {nome} é válido.')
            with open(r'D:\Projects\Estacio\Desenvolvimento Rápido Python\aula07\texto2.txt', 'w+') as file:
                file.write(f'{nome}\n')
            break
    except ValueError as e:
        print(f'Erro: {e}')
    except FileNotFoundError:
        print("Arquivo não encontrado.")