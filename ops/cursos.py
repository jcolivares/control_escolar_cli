from db import prompt, print_table

def consultar_cursos(conn):
    filtro = prompt("Filtrar por carrera (ENTER=Todas)").upper()

    sql = '''
    SELECT cu.clave, cu.nombre, cu.aula
    FROM cursos cu
    JOIN carreras ca ON ca.id_carrera = cu.id_carrera
    '''
    params = ()

    if filtro:
        sql += " WHERE ca.codigo=%s"
        params = (filtro,)

    with conn.cursor() as cur:
        cur.execute(sql, params)
        rows = cur.fetchall()

    print_table(["Clave","Curso","Aula"], rows)
