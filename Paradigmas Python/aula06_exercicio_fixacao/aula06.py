# Elabore um algoritmo em Linguagem de Programação em Python que imprima na tela os números e a quantidade de números pares, os números e a quantidade de ímpares e os números e a quantidade de múltiplos de 3 que existem entre 1 e 150.

quantidade_pares = 0
quantidade_impares = 0
quantidade_multiplos_tres = 0
lista_pares = []
lista_impares = []
lista_multiplos_tres = []

for i in range(1, 151):
    if (i % 2 == 0):
        quantidade_pares += 1
        lista_pares.append(i)
    if (i % 2 != 0):
        quantidade_impares += 1
        lista_impares.append(i)
    if (i % 3 == 0):
        quantidade_multiplos_tres += 1
        lista_multiplos_tres.append(i)

print(f'Quantidade de números pares no intervalo: \033[1;35m{quantidade_pares}\033[m\nNúmeros pares encontrados: \033[1;35m{lista_pares}\033[m')
print(f'\nQuantidade de números ímpares no intervalo: \033[1;35m{quantidade_impares}\033[m\nNúmeros pares encontrados: \033[1;35m{lista_impares}\033[m')
print(f'\nQuantidade de números múltiplos de 3 no intervalo: \033[1;35m{quantidade_multiplos_tres}\033[m\nNúmeros múltiplos de 3 encontrados: \033[1;35m{lista_multiplos_tres}\033[m')