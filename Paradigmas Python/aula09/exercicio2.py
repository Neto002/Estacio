class Pessoa(object):
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