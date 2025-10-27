
import configparser
from pathlib import Path

def load_config(filename='src/config/database.ini', section='postgresql') -> dict:
    """Функция возвращает параметры подключения к БД в виде словаря,
    без параметра database"""
    parser = configparser.ConfigParser()
    parser.read(Path(filename))
    if not parser.has_section(section):
        raise Exception(f'Section {section} not found in {filename}')
    params = dict(parser.items(section))
    return params

def get_db_connection_params(dbname: str) -> dict:
    """Функция принимает название базы данных и обновляет параметры добавляя параметр database,
    для подключения к базе данных"""
    params = load_config()
    params['database'] = dbname
    return params
