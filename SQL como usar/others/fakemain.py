# import minhasFuncoes
# import psycopg2

#postgress usando pgadmin4

# # Configurações do Banco de Dados
# host = "localhost"  # Endereço do servidor PostgreSQL
# port = "5432"       # Porta do PostgreSQL (padrão é 5432)
# user = "postgres"   # Substitua pelo seu usuário do PostgreSQL
# password = "Enquebravel11"  # Substitua pela sua senha do PostgreSQL
# database = "postgres"  # Conecte-se ao banco de dados padrão para criar um novo banco de dados

# # Nome do novo banco de dados
# database_name = "MarcaoPythonTeste"
# logica = 0

# def criandoSQL():
#     try:
#         # Conectando ao banco de dados padrão (por exemplo, 'postgres') para criar um novo banco de dados
#         conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
#         conn.autocommit = True  # Permitir criar o banco de dados sem precisar de uma transação

#         # Criando um cursor para executar comandos SQL
#         cursor = conn.cursor()

#         # Verificar se o banco de dados já existe
#         cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database_name}';")
#         db_exists = cursor.fetchone()

#         # Criar o banco de dados apenas se ele não existir
#         # if (not db_exists):
#         #     # Criar o banco de dados diretamente pelo Python
#         #     cursor.execute(f"CREATE DATABASE {database_name};")
#         #     print(f"Banco de dados '{database_name}' criado com sucesso.")
            
#         #     # Aguardar até que o novo banco de dados esteja disponível
#         #     for _ in range(10):  # Tentar até 10 vezes
#         #         try:
#         #             # Tentando conectar ao novo banco de dados
#         #             test_conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database_name)
#         #             test_conn.close()
#         #             print(f"Conexão ao banco de dados '{database_name}' estabelecida com sucesso.")
#         #             break
#         #         except psycopg2.OperationalError as e:
#         #             print(f"Aguardando o banco de dados '{database_name}' estar disponível... Erro: {e}")
#         #             time.sleep(1)
#         #     else:
#         #         raise Exception(f"Não foi possível conectar ao banco de dados '{database_name}' após a criação.")
#         # else:
#         #     print(f"Banco de dados '{database_name}' já existe.")

#         # Agora conectando-se ao novo banco de dados para criar a tabela
#         conn.close()  # Fechando a conexão inicial antes de abrir uma nova
#         conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database_name)
#         cursor = conn.cursor()

#         # Criando a tabela PROFESSOR
#         create_table_query = """
#         CREATE TABLE IF NOT EXISTS PROFESSOR (
#             RA SERIAL PRIMARY KEY,
#             nome VARCHAR(255) NOT NULL,
#             tipoProfessor INTEGER NOT NULL,
#             salario REAL NOT NULL
#         );
#         """
#         cursor.execute(create_table_query)
#         conn.commit()
#         print("Tabela 'PROFESSOR' criada com sucesso.")

#     except Exception as error:
#         print(f"Ocorreu um erro: {error}")

#     finally:
#         # Fechar a conexão
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# def main() -> bool:
#     # Início
#     biri = str(minhasFuncoes.chadNumero)
#     print(minhasFuncoes.minha_funcao(98) + biri)
#     criandoSQL()
#     # Final
#     return True

# main()
