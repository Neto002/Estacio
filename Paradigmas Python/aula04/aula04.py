#Criando Métodos
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
print(f'O valor do fatorial de {numero} é {calc_fatorial(numero)}')