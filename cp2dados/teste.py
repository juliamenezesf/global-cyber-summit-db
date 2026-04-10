from conexao import conectar

conn = conectar()

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM dual")
    print(cursor.fetchone())

    cursor.close()
    conn.close()