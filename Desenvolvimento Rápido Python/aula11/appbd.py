import psycopg2
#from main import PrincipalBD

class AppBD:
    def __init__(self):
        try:
            self.abrirConexao()
            #PrincipalBD.defineMensagemOperacao(self, "Conexão aberta com sucesso!")
            cursor = self.connection.cursor()
            postgres_create_table_query = """CREATE TABLE IF NOT EXISTS Produto (codigo int NOT NULL, nome VARCHAR(100) NOT NULL, preco FLOAT NOT NULL);"""
            cursor.execute(postgres_create_table_query)
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                pass
                #PrincipalBD.defineMensagemOperacao(self, f"Falha ao criar tabela no Banco de Dados: {error}")
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(database="exercicio_produto_db", user="postgres", password="postgres", host="127.0.0.1", port="5432")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                pass
                #PrincipalBD.defineMensagemOperacao(self, f"Falha ao se conectar ao Banco de Dados: {error}")
    
    def fecharConexao(self):
        if (self.connection):
            self.connection.close()
            #PrincipalBD.defineMensagemOperacao(self, "Conexão fechada com sucesso!")

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO Produto (codigo, nome, preco) VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            #PrincipalBD.defineMensagemOperacao(self, f"{count} registro(s) inserido(s) com sucesso!")
            #print(count, "Registro inserido com sucesso")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                #PrincipalBD.defineMensagemOperacao(self, f"Falha ao inserir dados no Banco de Dados: {error}")
                print("Falha ao inserir dados no Banco de Dados: ", error)
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_update_query = """UPDATE Produto SET nome = %s, preco = %s WHERE codigo = %s"""
            record_to_update = (nome, preco, codigo)
            cursor.execute(postgres_update_query, record_to_update)
            self.connection.commit()
            count = cursor.rowcount 
            #PrincipalBD.defineMensagemOperacao(self, f"{count} registro(s) atualizado(s) com sucesso!")
            postgres_select_query = "SELECT * FROM Produto WHERE codigo = %s"
            cursor.execute(postgres_select_query, (codigo,))
            record = cursor.fetchone()
            #PrincipalBD.defineMensagemOperacao(self, record)
        except (Exception, psycopg2.Error) as error:
            pass
            #PrincipalBD.defineMensagemOperacao(self, f"Falha ao atualizar dados no Banco de Dados: {error}")
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()
    
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_delete_query = """DELETE FROM Produto WHERE codigo = %s"""
            cursor.execute(postgres_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            #PrincipalBD().defineMensagemOperacao(self, f"{count} registro(s) excluído(s) com sucesso!")
        except (Exception, psycopg2.Error) as error:
            pass
            #PrincipalBD.defineMensagemOperacao(self, f"Falha ao excluir dados no Banco de Dados: {error}")
        finally:
            if (self.connection):
                cursor.close()
                self.fecharConexao()