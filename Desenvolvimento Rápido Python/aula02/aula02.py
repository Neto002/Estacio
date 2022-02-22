f = open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/texto.txt", 'w')
f.write("Texto 1")
f.close()


f = open("C:/Users/202102570735/Desktop/Estacio/Desenvolvimento Rápido Python/aula02/texto.txt", 'r')
print(f.read())
f.close()