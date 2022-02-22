# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/texto.txt", 'w') as f:
#     f.write("Texto 1\nTexto 2")

# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/texto.txt", 'r') as f:
#     print(f.read())
#     f.close()

# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/arquivo_jogadoresNFL.txt", 'r') as file:
#     print(file)
#     print(file.read())

# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/arquivo_teste.txt", 'r') as file:
#     for i in range(7):
#         print(file.readline())

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/arquivo_escrever.txt", 'w+') as f:
    texto = ["palavra 1", "palavra 2", "palavra 3"]

    for line in texto:
        f.write(line)
        f.write("\n")

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/arquivo_escrever.txt", 'r+') as f:
    print(texto)