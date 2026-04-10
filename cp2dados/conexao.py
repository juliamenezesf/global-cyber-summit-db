import oracledb

def conectar():
    try:
        connection = oracledb.connect(
            user="SEU_USUARIO",
            password="SUA_SENHA",
            dsn="SEU_DSN"
        )

        print("Conectado com sucesso!")
        return connection

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro Oracle: {error.code} - {error.message}")
        return None