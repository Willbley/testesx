
import csv
import pymysql

# Função para conectar ao banco de dados MySQL
def connect_to_mysql():
    return pymysql.connect(
        host='localhost',
        user='test_user',
        password='test_password',
        database='test_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


# Função para ler os dados do arquivo CSV e inseri-los no banco de dados
def insert_data_from_csv(file_path):
    connection = connect_to_mysql()
    cursor = connection.cursor()

    try:
        count = 0
        with open(file_path, newline='', encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                columns = ', '.join(row.keys())
                values = ', '.join(['%s'] * len(row))
                sql = f"INSERT INTO test_table ({columns}) VALUES ({values})"
                cursor.execute(sql, tuple(row.values()))
                count += 1
                if count % 10000 == 0:
                    connection.commit()
                    print(f"Registro {count} inserido com sucesso!")
        connection.commit()
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir os dados: {e}")
    finally:
        connection.close()

# Caminho para o arquivo CSV
file_path = 'DADOS/enem.csv'

# Chamada da função para inserir os dados no banco de dados
insert_data_from_csv(file_path)