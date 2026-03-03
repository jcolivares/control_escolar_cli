from db import prompt, print_table

def modificar_maestro(conn):
    sql = '''
    SELECT m.id_maestro, m.nombre, m.email
    FROM maestros m
    ORDER BY m.id_maestro
    '''
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()

    print_table(["ID","Nombre","Email"], rows)
    if not rows:
        return

    id_maestro = int(prompt("ID a modificar"))
    nuevo_nombre = prompt("Nuevo nombre")
    nuevo_email = prompt("Nuevo email")

    sql_upd = "UPDATE maestros SET nombre=%s, email=%s WHERE id_maestro=%s"

    try:
        with conn.cursor() as cur:
            cur.execute(sql_upd, (nuevo_nombre, nuevo_email, id_maestro))
        conn.commit()
        print("Maestro actualizado")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
