class Pessoa(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    
    def exibe_pessoa(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}')


pessoa1 = Pessoa('Neto', 19, 80)

print(pessoa1.exibe_pessoa())