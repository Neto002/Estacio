import psycopg2

class TelaPrincipal:
    pass

def main():
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", port="5432")
    print("Conexão com o banco de dados estabelecida com sucesso!")

    comando = conn.cursor()
    try:
        comando.execute("""CREATE TABLE Agenda (id INT PRIMARY KEY NOT NULL, nome VARCHAR(50) NOT NULL, telefone VARCHAR(12) NOT NULL)""")
        conn.commit()
        print("Tabela criada com sucesso!")
        conn.close()
    except (Exception, psycopg2.DatabaseError):
        print("Tabela já existe!")

if __name__ == "__main__":
    main()