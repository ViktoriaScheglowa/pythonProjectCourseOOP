from src.vacancies_class import Vacancy


def test_vacancy(init_vacancy: Vacancy, vacancy_data: dict):
    assert str(init_vacancy) == ('119764438Тестировщик QA '
                                 'https://api.hh.ru/vacancies/119764438?host=hh.ru '
                                 '100000 130000 Будет плюсом: – Опыт написания автотестов (UI и API), знание '
                                 '<highlighttext>Python</highlighttext> или JavaScript. – Владение '
                                 'инструментами для автоматизации (Selenium, Pytest, Playwright и...')
    assert isinstance(Vacancy.get_vacancy([vacancy_data]), list)
