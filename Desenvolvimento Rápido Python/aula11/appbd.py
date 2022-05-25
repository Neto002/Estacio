import psycopg2

class AppBD:
    def __init__(self):
        try:
            self.abrirConexao()
            print("Conexão aberta com sucesso!")
            cursor = self.connection.cursor()
            postgres_create_table_query = """CREATE TABLE IF NOT EXISTS Produto (id serial NOT NULL, codigo VARCHAR(10) NOT NULL, nome VARCHAR(100) NOT NULL, preco FLOAT NOT NULL);"""
            cursor.execute(postgres_create_table_query)
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao criar tabela no Banco de Dados: ", error)
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(database="exercicio_produto_db", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados: ", error)
    
    def fecharConexao(self):
        if (self.connection):
            self.connection.close()
            print("Conexão fechada com sucesso!")

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."Produto" ("codigo", "nome", "preco") VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir dados no Banco de Dados: ", error)
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()