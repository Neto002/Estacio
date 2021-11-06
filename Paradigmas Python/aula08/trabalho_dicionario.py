'''# Elabore um script em Python que leia uma String e conte a quantidade de ocorrências de caracteres dessa string

string = str(input('Digite aqui qualquer coisa para a análise: ')).strip()

dicionario = {}
for i in range(len(string)):
    dicionario.update({string[i]:string.count(string[i])} if string[i] != ' ' else {'espaço vazio':string.count(string[i])})

print(f'A string "{string}" tem ', end='')
c = 0
for i, j in dicionario.items():
    c += 1
    print(f'{j} - {i}, ' if c < len(dicionario) else f'e {j} - {i}.', end='')

# Elabore um script em Python que leia um dicionário 1 e apresente um novo dicionário 2 com os tamanhos dos valores do dicionário 1

lista = [(int(input('Chave 1: ')), input('Valor 1: ')), (int(input('Chave 2: ')), input('Valor 2: ')), (int(input('Chave 3: ')), input('Valor 3: ')), (int(input('Chave 4: ')), input('Valor 4: ')), (int(input('Chave 5: ')), input('Valor 5: '))]

dicionario1 = dict(lista)

dicionario2 = {}

for i, j in dicionario1.items():
    dicionario2.update({j:len(j)})

print(dicionario2)

# Converter duas listas em elementos de um dicionário

chaves = [input('Chave 1: '), input('Chave 2: '), input('Chave 3: ')]
valores = [input('Valor 1: '), input('Valor 2: '), input('Valor 3: ')]

dicionario = {}

for i in range(3):
    dicionario.update({chaves[i]:valores[i]})

print(dicionario)'''
