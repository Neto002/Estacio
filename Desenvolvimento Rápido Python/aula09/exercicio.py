import sqlite3

connection = sqlite3.connect('exercicio.db')

table = connection.cursor()

table.execute("""CREATE TABLE pessoas (cpf, nome, rg, data_nasc);""")

cpf = input('Digite o CPF: ').strip()

while True:
    if not cpf.isnumeric() or len(cpf) != 11:
        cpf = input('Digite o CPF: ').strip()
    else:
        break

nome = input('Digite o nome: ').strip().title()

rg = input('Digite o RG: ').strip()

data_nasc = input('Digite a data de nascimento: ').strip()

print(cpf, nome, rg, data_nasc)

print("Adicionando registro ao banco de dados...")

table.execute(f"""INSERT INTO pessoas VALUES ('{cpf}', '{nome}', '{rg}', '{data_nasc}');""")

connection.commit()

print("Registro adicionado com sucesso!")
print(tuple(table.execute(f"""SELECT * FROM pessoas;""")))