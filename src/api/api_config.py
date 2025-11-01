"""
Модуль конфигурации для работы с API HeadHunter.
Содержит настройки и параметры для взаимодействия с API.
"""

# Базовый URL API HeadHunter
BASE_URL = 'https://api.hh.ru'

# Заголовки для запросов к API
HEADERS = {
    'User-Agent': 'HeadHunterDB Project/1.0 (automag2016@mail.ru)',
    'Accept': 'application/json'
}

# Список ID компаний для сбора вакансий
# Можно расширить список добавив другие компании
COMPANY_IDS = [
    '1740',  # Яндекс
    '3529',  # Сбербанк
    '15478',  # VK
    '2180',  # OZON
    '78638',  # Тинькофф
    '1122462',  # Авито
    '1122462',  # Kaspersky
    '1740',  # Positive Technologies
    '4181',  # МТС
    '3776',  # СИБУР
]

# Параметры запроса для получения вакансий
VACANCY_PARAMS = {
    'per_page': '100',  # Количество вакансий на странице
    'page': '0',  # Номер страницы
    'area': '113',  # Код региона (113 - Россия)
    'only_with_salary': 'true'  # Только вакансии с указанной зарплатой
}

# Параметры запроса для получения информации о компании
COMPANY_PARAMS = {
    'area': '113',  # Код региона
    'per_page': '100'  # Количество результатов на странице
}

# Настройки для обработки запросов
REQUEST_SETTINGS = {
    'timeout': 5,  # Таймаут запроса в секундах
    'max_retries': 3,  # Максимальное количество повторных попыток
    'retry_delay': 1  # Задержка между повторными попытками в секундах
}

# Ключевые слова для поиска вакансий
SEARCH_KEYWORDS = [
    'Python',
    'SQL',
    'PostgreSQL',
    'Django',
    'Flask',
    'FastAPI'
]

# Параметры для фильтрации вакансий
VACANCY_FILTERS = {
    'experience': 'noExperience',  # Опыт работы
    'employment': 'full',  # Тип занятости
    'schedule': 'remote',  # График работы
    'order_by': 'publication_time'  # Сортировка
}


def get_company_url(company_id: str) -> str:
    """
    Формирует URL для получения информации о компании.

    Args:
        company_id (str): ID компании

    Returns:
        str: Полный URL для API-запроса
    """
    return f"{BASE_URL}/employers/{company_id}"


def get_vacancies_url(company_id: str) -> str:
    """
    Формирует URL для получения вакансий компании.

    Args:
        company_id (str): ID компании

    Returns:
        str: Полный URL для API-запроса
    """
    return f"{BASE_URL}/vacancies?employer_id={company_id}"


def get_search_url() -> str:
    """
    Формирует URL для поиска вакансий.

    Returns:
        str: Полный URL для API-запроса
    """
    return f"{BASE_URL}/vacancies"

