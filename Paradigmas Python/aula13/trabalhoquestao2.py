def soma_consecutivo(n):
    if n >= 1:
        return soma_consecutivo(n - 1) + n
    return n

numero = int(input('Digite um número: '))

for i in range(1, numero + 1):
    print(f'{i} + ' if i < numero else f'{i} = {soma_consecutivo(numero)}', end='')