import psycopg2

global POSTGRES_CREATE_TABLE_QUERY, POSTGRES_INSERT_QUERY, POSTGRES_UPDATE_QUERY, POSTGRES_SELECT_QUERY, POSTGRES_DELETE_QUERY
POSTGRES_CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS public.produto (codigo integer NOT NULL, nome text NOT NULL, preco money NOT NULL)"""
POSTGRES_INSERT_QUERY = """INSERT INTO public.produto (codigo, nome, preco) VALUES (%s, %s, %s)"""
POSTGRES_UPDATE_QUERY = """UPDATE public.produto SET nome = %s, preco = %s WHERE codigo = %s"""
POSTGRES_SELECT_QUERY = """SELECT * FROM public.produto WHERE codigo = %s"""
POSTGRES_DELETE_QUERY = """DELETE FROM public.produto WHERE codigo = %s"""

class AppBD:
    def __init__(self):
        self.criarTabela()
    
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print(f"Falha ao se conectar ao Banco de Dados: {error}")
    
    def criarTabela(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            cursor.execute(POSTGRES_CREATE_TABLE_QUERY)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao criar tabela no Banco de Dados: ", error)
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def fecharConexao(self):
        self.connection.close()

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            record_to_insert = (codigo, nome, preco)
            cursor.execute(POSTGRES_INSERT_QUERY, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "registro inserido com sucesso")
            cursor.execute(POSTGRES_SELECT_QUERY, (codigo,))
            return cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir dados no Banco de Dados: ", error)
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            record_to_update = (nome, preco, codigo)
            cursor.execute(POSTGRES_UPDATE_QUERY, record_to_update)
            self.connection.commit()
            count = cursor.rowcount 
            print(f"{count} registro(s) atualizado(s) com sucesso!")
            cursor.execute(POSTGRES_SELECT_QUERY, (codigo,))
            record = cursor.fetchone()
            return (record)
        except (Exception, psycopg2.Error) as error:
            print(f"Falha ao atualizar dados no Banco de Dados: {error}")
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            cursor.execute(POSTGRES_DELETE_QUERY, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(f"{count} registro(s) excluído(s) com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print(f"Falha ao excluir dados no Banco de Dados: {error}")
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()