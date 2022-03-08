def palindromo():
    string = input("Digite a palavra ou frase: ").strip().replace(" ", "").lower()
    if string == string[::-1]:
        return "É palíndromo"
    else:
        return "Não é palíndromo"

print(palindromo())