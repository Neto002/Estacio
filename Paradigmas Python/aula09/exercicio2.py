'''class Pessoa(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    def andar(self):
        print('anda')

pessoa1 = Pessoa("Juliana", 23, 75)
pessoa2 = Pessoa("Carlos", 39, 72)

print(pessoa1.nome)
pessoa1.andar()

def fatorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n-1) * n

print(fatorial(5))'''

S = [2*x for x in range(101) if x%2==0]
A = [x**2+x+1 for x in range(100) if x%2==0]
print(S)
print(A)