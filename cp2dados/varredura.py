from cp2dados.conexao import conectar
import oracledb

def executar_varredura():
    conn = conectar()

    if conn:
        cursor = conn.cursor()

        plsql_block = """
        DECLARE
            CURSOR c_inscricoes IS
                SELECT i.id, i.usuario_id, u.email
                FROM inscricoes i
                JOIN usuarios u ON i.usuario_id = u.id
                WHERE i.status = 'PENDING';

            v_id_inscricao inscricoes.id%TYPE;
            v_usuario_id usuarios.id%TYPE;
            v_email usuarios.email%TYPE;

        BEGIN
            OPEN c_inscricoes;

            LOOP
                FETCH c_inscricoes INTO v_id_inscricao, v_usuario_id, v_email;
                EXIT WHEN c_inscricoes%NOTFOUND;

                IF v_email LIKE '%@fake.com%'
                   OR v_email LIKE '%@temp-mail%'
                   OR NOT REGEXP_LIKE(v_email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
                THEN

                    UPDATE inscricoes
                    SET status = 'CANCELLED'
                    WHERE id = v_id_inscricao;

                    UPDATE usuarios
                    SET trust_score = trust_score - 15
                    WHERE id = v_usuario_id;

                    INSERT INTO log_auditoria (id, inscricao_id, motivo, data)
                    VALUES (log_auditoria_seq.NEXTVAL,
                            v_id_inscricao,
                            'Fraude detectada',
                            SYSDATE);

                END IF;

            END LOOP;

            CLOSE c_inscricoes;

            COMMIT;

        EXCEPTION
            WHEN OTHERS THEN
                ROLLBACK;
        END;
        """

        try:
            cursor.execute(plsql_block)
            print("Varredura executada com sucesso!")

        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Erro Oracle: {error.code} - {error.message}")

        finally:
            cursor.close()
            conn.close()