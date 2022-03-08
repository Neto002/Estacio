'''def palindromo():
    string = input("Digite a palavra ou frase: ").strip().replace(" ", "").lower()
    if string == string[::-1]:
        return "É palíndromo"
    else:
        return "Não é palíndromo"

print(palindromo())'''

# Elabore um programa em Python que leia uma cadeia de DNA e gera a cadeia inversa. Faça a leitura da cadeia utilizando arquivo txt. Exemplo:
# Entrada: AATCTGCAC
# Saída: CACGTCTAA

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/dna.txt", "w+") as file:
    dna = input("Digite a cadeia de DNA para análise: ").strip().upper()
    file.write(f"Cadeia normal: {dna}\n")
    file.write(f"Cadeia invertida: {dna[::-1]}\n")

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/dna.txt", "r+") as file:
    print(file.read())