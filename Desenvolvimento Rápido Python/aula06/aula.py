# Tratamento de Exceções

# Exercícios

# Exemplo 1: Divisão por zero.

while True:
    try:
        numerador = int(input('Digite um numerador: '))
        denominador = int(input('Digite um denominador: '))
        divisao = numerador/denominador
        print(f'A divisão entre os dois números é: {divisao}')
        break
    except ZeroDivisionError:
        print('O denominador deve ser diferente de 0.')

# Exemplo 2: Soma de tipos não suportados.

while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        soma = n1 + n2
        print(f'A soma é: {soma}')
        break
    except TypeError:
        print('Os dois termos precisam ser números.')
    except ValueError:
        print('Os dois termos precisam ser números.')

# Exemplo 3: Acesso a índices inexistentes.

lista = [1, 2, 3]
while True:
    try:
        index = int(input('Digite um índice para printar: '))
        print(lista[index])
        break
    except IndexError:
        print(f'O índice {index} não existe na lista.')

# Exemplo 4: Acesso a chaves inexistentes.

dicionario = {1:"item 1", 2:"item 2"}

while True:
    try:
        chave = int(input("Digite uma chave para exibir: "))
        print(dicionario[chave])
        break
    except KeyError:
        print(f"A chave {chave} não existe no dicionário.")

# Exemplo 5: Erros de Sintaxe (mais comuns).

#while True print("Hello World")

# Exemplo 6: Erros de nomes (variáveis) ou a falta delas.

try:
    print(4 + spam*3)
except NameError:
    print("Variável não definida anteriormente.")

# Exemplo 7: Tentativa de concatenaçãode tipos diferentes.

try:
    print('2' + 2)
except TypeError:
    print("Não é possível concatenar strings com valores tipo int.")

# Exemplo 8: Tentativa de operaçãode tipos diferentes.

try:
    print(2 + '2')
except TypeError:
    print("Não é possível somar valores tipo int com strings.")

# Exemplo 9: Usar uma biblioteca que não foi invocada antes.

try:
    print(math.sqrt(2))
except NameError:
    print("Biblioteca não foi importada.")

# Exemplo 10: Erros associados à cálculos matemáticos.

import math

try:
    print(math.sqrt(-2))
except ValueError:
    print("Não existe raiz quadrada para o valor especificado.")

# Exemplo 11: Tentativa de abrir um arquivo para leitura.

try:
    print("Abrindo um arquivo!")
    open("texto.txt", "r")
except FileNotFoundError:
    print("O arquivo especificado não existe.")

# Exemplo 2 de uso do try/except:

'''import math

num = -2

try:
    resultado = math.sqrt(num)
    print(f'Raiz quadrada: {resultado}')
except ValueError:
    num = -num
    print("Transformando número negativo em positivo")
    resultado = math.sqrt(num)
    print(f'Raiz quadrada: {resultado}')'''

# Exemplo 5 de uso do try/except:

'''def dividir():
    try:
        x = int(input("Primeiro número: "))
        y = int(input("Segundo número: "))
        resultado = x/y
    except ZeroDivisionError:
        print("Divisão por zero!")
    except ValueError:
        print("Dado informado inválido!")
    else:
        print(f"Resultado: {resultado}")

dividir()'''

