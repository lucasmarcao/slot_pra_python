import mysql
import mysql.connector

# tipo url SQL:
# value="jdbc:mysql://localhost:3336/banco_ben10_java
# ?zeroDateTimeBehavior=convertToNull"/
# conta MySQL:  root
# senha MySQL: LucasMarcao1
bancoDeDados = mysql.connector.connect(
    host='localhost',
    database='cadeia',
    user='root',
    port='3336',
    password='LucasMarcao1'
)

# inicio comandos


def verificaSeFuncionaMySQL() -> None:

    if bancoDeDados.is_connected():
        db_info = bancoDeDados.get_server_info()
        print("Conectado ao servidor MySQL version ", db_info)
        cursor = bancoDeDados.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)
    if bancoDeDados.is_connected():
        cursor.close()
        print("\n fechou. \n")
        bancoDeDados.close()

# funcões de controle CRUD auxiliar


def selecionarBD() -> int:
    query = '''
    SELECT * FROM cadeia.prisioneiro;
    '''
    cursor = bancoDeDados.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n")
    for row in result:
        print(row)
    print("\n")
    return 1


def inserirNaTabelaPrisioneiro() -> int:
    query = '''
    INSERT INTO `cadeia`.`prisioneiro` 
    (`id_prisioneiro`, `nome`, `raca`, `data_de_entrada`) 
    VALUES ('12', 'juinio clara', 'gugu didi', '2000-11-06');
    '''
    # data = ano mes dia
    cursor = bancoDeDados.cursor()
    cursor.execute(query)
    bancoDeDados.commit()
    print("\n")
    return 1
# clases
