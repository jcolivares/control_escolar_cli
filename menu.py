from db import prompt
from ops.carreras import agregar_carrera
from ops.maestros import modificar_maestro
from ops.alumnos import borrar_alumno
from ops.cursos import consultar_cursos

def run_menu(conn):
    while True:
        print("\n=== Control Escolar ITM ===")
        print("1) Agregar carrera")
        print("2) Modificar maestro")
        print("3) Borrar alumno")
        print("4) Consultar cursos")
        print("0) Salir")

        op = prompt("Opción", "0")

        if op == "1":
            agregar_carrera(conn)
        elif op == "2":
            modificar_maestro(conn)
        elif op == "3":
            borrar_alumno(conn)
        elif op == "4":
            consultar_cursos(conn)
        elif op == "0":
            break
        else:
            print("Opción inválida")
