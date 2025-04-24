from src.vacancies_class import Vacancy


def test_vacancy(init_vacancy: Vacancy, vacancy_data: dict) -> None:
    assert str(init_vacancy) == ("119602010Тестировщик (QA-инженер) https://api.hh.ru/vacancies/119602010?host=hh.ru 1 10000 Знакомство с Postman и умение составлять API запросы. Знание основ HTML, CSS, JS, <highlighttext>Python</highlighttext>. Опыт написания тестовой документации (тест-кейсы...")
    assert isinstance(Vacancy.get_vacancy([vacancy_data]), list)
