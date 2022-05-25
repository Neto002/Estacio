import psycopg2

global postgres_create_table_query, postgres_insert_query, postgres_update_query, postgres_select_query, postgres_delete_query
postgres_create_table_query = """CREATE TABLE IF NOT EXISTS public.produto (codigo integer NOT NULL, nome text NOT NULL, preco money NOT NULL)"""
postgres_insert_query = """INSERT INTO public.produto (codigo, nome, preco) VALUES (%s, %s, %s)"""
postgres_update_query = """UPDATE public.produto SET nome = %s, preco = %s WHERE codigo = %s"""
postgres_select_query = """SELECT * FROM public.produto WHERE codigo = %s"""
postgres_delete_query = """DELETE FROM public.produto WHERE codigo = %s"""

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
            #postgres_create_table_query = """CREATE TABLE IF NOT EXISTS public.produto (codigo integer NOT NULL, nome text NOT NULL, preco double precision NOT NULL)"""
            cursor.execute(postgres_create_table_query)
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
            #postgres_insert_query = """INSERT INTO public.produto (codigo, nome, preco) VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "registro inserido com sucesso")
            cursor.execute(postgres_select_query, (codigo,))
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
            #postgres_update_query = """UPDATE public.produto SET nome = %s, preco = %s WHERE codigo = %s"""
            record_to_update = (nome, preco, codigo)
            cursor.execute(postgres_update_query, record_to_update)
            self.connection.commit()
            count = cursor.rowcount 
            print(f"{count} registro(s) atualizado(s) com sucesso!")
            #postgres_select_query = "SELECT * FROM public.produto WHERE codigo = %s"
            cursor.execute(postgres_select_query, (codigo,))
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
            #postgres_delete_query = """DELETE FROM public.produto WHERE codigo = %s"""
            cursor.execute(postgres_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(f"{count} registro(s) excluído(s) com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print(f"Falha ao excluir dados no Banco de Dados: {error}")
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()