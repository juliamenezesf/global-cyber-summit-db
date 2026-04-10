import oracledb

def conectar():
    try:
        connection = oracledb.connect(
            user="DB_USER",
            password="DB_PASSWORD",
            dsn="DB_DSN"
        )

        print("Conectado com sucesso!")
        return connection

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro Oracle: {error.code} - {error.message}")
        return None