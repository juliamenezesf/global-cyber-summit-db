import os
import oracledb

def conectar():
    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER") or "SEU_USUARIO",
            password=os.getenv("DB_PASSWORD") or "SUA_SENHA",
            dsn=os.getenv("DB_DSN") or "oracle.fiap.com.br:1521/ORCL"
        )

        print("Conectado com sucesso!")
        return connection

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro Oracle: {error.code} - {error.message}")
        return None