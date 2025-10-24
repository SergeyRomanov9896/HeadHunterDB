
import psycopg2

from src.config.config import get_db_connection_params
from src.DBManager import DBManager
from src.create_database import create_database

def main():
    """Программа для получения данных компаний и их вакансий"""

    # При запуске приложения спрашивать 10 названий компаний, если хотя бы одно повторяется – приложения предлагает выбрать,
    # какую именно компанию скачивать в локальную базу.

    db_manager = DBManager()  # Класс базы данных
    create_database(dbname=db_manager.dbname) # Создание базы данных
    db_params = get_db_connection_params(dbname=db_manager.dbname) # Конфиг
    DBManager.create_table() # Создание таблиц


if __name__ == '__main__':
    main()