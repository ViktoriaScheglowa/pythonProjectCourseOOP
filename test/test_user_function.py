from _pytest.capture import CaptureFixture

from src.user_function import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies
from src.vacancies_class import Vacancy


def test_user_function(capsys: CaptureFixture, init_vacancy):
    data: list[Vacancy] = [init_vacancy]
    words = "python".split()
    assert filter_vacancies(data, words) == []

    assert get_vacancies_by_salary(data, "1-1000")[0].name == "Тестировщик QA"
    assert sort_vacancies(data)[0].id_vacancy == "119764438"
    assert get_top_vacancies(data, 1)[0].id_vacancy == "119764438"
    print_vacancies(data)
    read_out = capsys.readouterr()
    assert read_out.out == ('119764438Тестировщик QA https://api.hh.ru/vacancies/119764438?host=hh.ru 1 '
                            '1000 Будет плюсом: – Опыт написания автотестов (UI и API), знание '
                            '<highlighttext>Python</highlighttext> или JavaScript. – Владение '
                            'инструментами для автоматизации (Selenium, Pytest, Playwright и...\n')
