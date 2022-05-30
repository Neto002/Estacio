# Parte 3 Exercício 3

class Calculadora:
    def __init__(self, A, B):
        self.a = A
        self.b = B

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b

# Programa principal

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))

calc = Calculadora(a, b)

somaCalculadora = calc.somar()
subtracaoCalculadora = calc.subtrair()
multiplicacaoCalculadora = calc.multiplicar()
divisaoCalculadora = calc.dividir()

print(f"Soma: {somaCalculadora}")
print(f"Subtração: {subtracaoCalculadora}")
print(f"Multiplicação: {multiplicacaoCalculadora}")
print(f"Divisão: {divisaoCalculadora}")