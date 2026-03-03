import mysql.connector
import conexiones

def get_db_config():
    return {
        "host": conexiones.DB_HOST,
        "port": conexiones.DB_PORT,
        "user": conexiones.DB_USER,
        "password": conexiones.DB_PASS,
        "database": conexiones.DB_NAME,
    }

def connect():
    return mysql.connector.connect(**get_db_config())

def prompt(msg, default=None):
    if default:
        msg = f"{msg} [{default}]: "
    else:
        msg = f"{msg}: "
    val = input(msg).strip()
    return val if val else (default or "")

def print_table(headers, rows):
    if not rows:
        print("(sin resultados)")
        return
    widths = [len(h) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(str(cell)))
    def fmt(row):
        return " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row)))
    print(fmt(headers))
    print("-+-".join("-"*w for w in widths))
    for r in rows:
        print(fmt(r))
