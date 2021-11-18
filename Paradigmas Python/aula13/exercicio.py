'''#Instanciação classe Pessoa

class Pessoa(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    def andar(self):
        print(f'{self.nome} está andando.')
    def dormir(self):
        print(f'{self.nome} está dormindo.')

pessoa1 = Pessoa("Juliana", 23, 75)
pessoa2 = Pessoa("Carlos", 39, 72)

#Calculadora

class Calculadora(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.a / self.b

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

calc = Calculadora(a, b)
print(f'Soma: {calc.somar()}\nSubtração: {calc.subtrair()}\nMultiplicação: {calc.multiplicar()}\nDivisão: {calc.dividir()}')

#Lista

print([x for x in range(5, 101) if x%7==0 and x%5!=0])

#Salario

salario = float(input('Digite seu salário: '))
porcentagem = 0.15 if salario < 500 else 0.10 if salario >= 500 and salario <= 1000 else 0.05

print(f'Seu novo salário é de R${salario + (salario*porcentagem):.2f}')'''

nome = "12345678911111111111"
print(nome[:9])