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