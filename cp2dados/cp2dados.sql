
BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE log_auditoria CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE inscricoes CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE usuarios CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP SEQUENCE log_auditoria_seq';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/



CREATE TABLE usuarios (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(100),
    email VARCHAR2(100),
    prioridade NUMBER,
    saldo NUMBER,
    trust_score NUMBER
);

CREATE TABLE inscricoes (
    id NUMBER PRIMARY KEY,
    usuario_id NUMBER,
    status VARCHAR2(20),
    valor_pago NUMBER,
    tipo VARCHAR2(50),
    CONSTRAINT fk_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
);

CREATE TABLE log_auditoria (
    id NUMBER PRIMARY KEY,
    inscricao_id NUMBER,
    motivo VARCHAR2(200),
    data DATE
);



CREATE SEQUENCE log_auditoria_seq
START WITH 1
INCREMENT BY 1;



INSERT INTO usuarios VALUES (1, 'Ana', 'ana@fake.com', 1, 100, 100);
INSERT INTO usuarios VALUES (2, 'Carlos', 'carlos@email.com', 2, 200, 100);

INSERT INTO inscricoes VALUES (1, 1, 'PENDING', 50, 'VIP');
INSERT INTO inscricoes VALUES (2, 2, 'PENDING', 50, 'NORMAL');

COMMIT;



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
           OR v_email NOT LIKE '%@%.%'
        THEN

            INSERT INTO log_auditoria (id, inscricao_id, motivo, data)
            VALUES (
                log_auditoria_seq.NEXTVAL,
                v_id_inscricao,
                'Fraude detectada - penalidade de 15 pontos no trust_score | Email: ' || v_email,
                SYSDATE
            );

        END IF;

    END LOOP;

    CLOSE c_inscricoes;

    COMMIT;

EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
END;
/



SELECT * FROM usuarios;
SELECT * FROM inscricoes;
SELECT * FROM log_auditoria;