from db import prompt

def borrar_alumno(conn):
    matricula = prompt("Matrícula").upper()
    if not matricula:
        return

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id_alumno FROM alumnos WHERE matricula=%s", (matricula,))
            row = cur.fetchone()
            if not row:
                print("No encontrado")
                return
            id_alumno = row[0]
            cur.execute("DELETE FROM inscripciones WHERE id_alumno=%s", (id_alumno,))
            cur.execute("DELETE FROM alumnos WHERE id_alumno=%s", (id_alumno,))
        conn.commit()
        print("Alumno eliminado")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
