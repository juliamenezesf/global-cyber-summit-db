import os
import oracledb

def conectar():
    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

        print("Conectado com sucesso!")
        return connection

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro Oracle: {error.code} - {error.message}")
        return None