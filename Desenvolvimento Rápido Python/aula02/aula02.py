# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/texto.txt", 'w') as f:
#     f.write("Texto 1\nTexto 2")

# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/texto.txt", 'r') as f:
#     print(f.read())
#     f.close()

# with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/arquivo_jogadoresNFL.txt", 'r') as file:
#     print(file)
#     print(file.read())

with open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/arquivo_teste.txt", 'r') as file:
    for line in file:
        print(file.readline())