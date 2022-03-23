class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    
    def exibe_pessoa(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}')

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def somar(self):
        return self.a+self.b
    
    def subtrair(self):
        return self.a-self.b
    
    def multiplicar(self):
        return self.a*self.b
    
    def dividir(self):
        return self.a/self.b

def main():
    pessoa1 = Pessoa('Neto', 19, 80)
    print(pessoa1.exibe_pessoa())

    calculadora = Calculadora(2, 2)
    print(calculadora.somar())

if '__name__' == '__main__':
    main()