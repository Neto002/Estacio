import sqlite3

connection = sqlite3.connect('aula09.db')
tabela = connection.cursor()

tabela.execute("""CREATE TABLE dados (nome, rg, cpf, data_nasc);""")
tabela.execute("""INSERT INTO dados VALUES ('João', '123456789', '123456789', '01/01/2000');""")

dados = [('João', '123456789', '123456789', '01/01/2000'), ('João', '123456789', '123456789', '01/01/2000')]

tabela.executemany("INSERT INTO dados VALUES (?, ?, ?, ?);", dados)
connection.commit

tabela.execute("DELETE FROM dados WHERE nome = 'João'")
connection.commit()

print("Lista de todos os registros da tabela:\n")
for i in tabela.execute("SELECT rowid, * FROM dados ORDER BY nome"):
    print(i)