from db import prompt

def agregar_carrera(conn):
    codigo = prompt("Código").upper()
    nombre = prompt("Nombre")

    if not codigo or not nombre:
        print("Datos obligatorios")
        return

    sql = "INSERT INTO carreras (codigo, nombre) VALUES (%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (codigo, nombre))
        conn.commit()
        print("Carrera agregada")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
