
import psycopg2
from config.config import load_config

def create_database(dbname: str):
    """Функция для создания новой базы данных"""
    params = load_config()
    conn = psycopg2.connect(**params, database='postgres')
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE DATABASE {dbname};")
        print(f"База данных {dbname}, создана.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"База данных {dbname}, уже существует.")
    finally:
        cur.close()
        conn.close()

