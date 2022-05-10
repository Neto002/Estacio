import sqlite3

connection = sqlite3.connect('aula09.db')
tabela = connection.cursor()

tabela.execute("""CREATE TABLE dados (id, nome, rg, cpf, data_nasc);""")
tabela.execute("""INSERT INTO dados VALUES (1, 'João', '123456789', '123456789', '01/01/2000');""")

connection.commit()

dados = tuple(tabela.execute("""SELECT * FROM dados;"""))

print(dados)