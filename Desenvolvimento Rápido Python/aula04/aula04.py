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

'''with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/dna.txt", "w+") as file:
    dna = input("Digite a cadeia de DNA para análise: ").strip().upper()
    file.write(f"Cadeia normal: {dna}\n")
    file.write(f"Cadeia invertida: {dna[::-1]}\n")

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/dna.txt", "r+") as file:
    print(file.read())'''

# Faça um programa que leia um texto de um arquivo txt e conte quantas palavras tem nesse arquivo, sem considerar os espaços.

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/textos.txt", "r+") as file:
    texto_arquivo = str(file.read())
    lista = texto_arquivo.split()
    print(f'O texto contido no arquivo tem {len(lista)}', 'palavras.' if len(lista) > 1 else 'palavra.')