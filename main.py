from db import connect, get_db_config
from menu import run_menu
from mysql.connector import Error
import sys

def main():
    try:
        conn = connect()
    except Error as e:
        print(f"No se pudo conectar a MySQL: {e}")
        sys.exit(1)

    print("Conectado a BD:", get_db_config()["database"])

    try:
        run_menu(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
