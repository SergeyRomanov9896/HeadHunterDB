

def get_employer(employer_id: str) -> dict:
    """Получает данные о компании по её ID."""
    pass


def get_vacancies(employer_id: str, page: int = 0) -> dict:
    """Получает вакансии компании по её ID и номеру страницы."""
    pass


def fetch_all_vacancies_for_employer(employer_id: str) -> list[dict]:
    """Получает все вакансии компании с учётом пагинации."""
    pass
