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

'''with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/textos.txt", "r+") as file:
    texto_arquivo = str(file.read())
    lista = texto_arquivo.split()
    print(f'O texto contido no arquivo tem {len(lista)}', 'palavras.' if len(lista) > 1 else 'palavra.')'''

# Faça um programa que Python que lê um texto de um arquivo txt e substitua todos os espaços por underline (_).

'''with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula04/textos.txt", "r+") as file:
    texto_arquivo_formatado = str(file.read()).replace(" ", "_")
    print(texto_arquivo_formatado)'''

# Execute um algoritmo em Python que, tendo o nome completo de uma pessoa, forme o seu email institucional. Exemplo:
# Nome: Maria José;
# Email: maria.empresa@gmail.com

'''nome = input("Digite seu nome completo: ").strip().lower()
nome_formatado = nome.replace(" ", ".")
email = f"{nome_formatado}.empresa@gmail.com"
print(email)'''

# Elabore um programa que leia duas strings e verifique se elas são palíndromos mútuos, ou seja, se uma é igual à outra quando lida de traz para frente. Exemplo: amor e roma.