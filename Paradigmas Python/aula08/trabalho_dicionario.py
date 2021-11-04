# Elabore um script em Python que leia uma String e conte a quantidade de ocorrências de caracteres dessa string

string = str(input('Digite aqui qualquer coisa para a análise: ')).strip()
i = 0

dicionario = {}
for i in range(len(string)):
    dicionario.update({string[i]:string.count(string[i])} if string[i] != ' ' else {'espaço vazio':string.count(string[i])})

print(f'A string "{string}" tem ', end='')
c = 0
for i, j in dicionario.items():
    c += 1
    print(f'{j} - {i}, ' if c < len(dicionario) else f'e {j} - {i}.', end='')

# Elabore um script em Python que leia um dicionário 1 e apresente um novo dicionário 2 com os tamanhos dos valores do dicionário 1

# Converter duas listas em elementos de um dicionário,