
import requests

def uploading_vacancies() -> list[dict]:
    """
    Получает первые 10 компаний (работодателей) с публичного API hh.ru.

    :return: Список словарей с информацией о компаниях.
    """

    url = 'https://api.hh.ru/employers'

    headers = {
        "User-Agent": "MyApp/1.0 (automag2016@mail.ru)"
    }

    params = {
        "per_page": 10,  # количество компаний на странице
        "page": 0,  # номер страницы (начинаем с первой)
        "sort_by": "by_vacancies_open"  # сортировка по количеству открытых вакансий
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print(f"Ошибка при запросе: {response.status_code}")
        return []
