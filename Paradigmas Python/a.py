def contaTamanho(numero):
    tamanhoNumero = len(str(numero))
    print(f"O número digitado tem {tamanhoNumero} dígitos")

num = int(input("Digite um número: "))
contaTamanho(num)