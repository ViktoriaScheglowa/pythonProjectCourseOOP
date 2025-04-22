import pytest
from src.file_handler_class import FileHandler
from src.hh_class import HH
from src.vacancies_class import Vacancy


@pytest.fixture
def vacancy_data():
    return {'119764438Тестировщик QA https://api.hh.ru/vacancies/119764438?host=hh.ru 100000 130000 Будет плюсом: – Опыт написания автотестов (UI и API), знание '
                                     '<highlighttext>Python</highlighttext> или JavaScript. – Владение '
                                     'инструментами для автоматизации (Selenium, Pytest, Playwright и...'}


@pytest.fixture
def init_hh():
    return HH()


@pytest.fixture
def init_file_handler():
    return FileHandler("test.json")


@pytest.fixture
def init_vacancy():
    return Vacancy(**{
        "id_vacancy": "119764438",
        "name": "Тестировщик QA",
        "url": "https://api.hh.ru/vacancies/119764438?host=hh.ru",
        "salary_from": 100000,
        "salary_to": 130000,
        "requirement": "Будет плюсом: – Опыт написания автотестов (UI и API), знание <highlighttext>Python</highlighttext> или JavaScript. – Владение инструментами для автоматизации (Selenium, Pytest, Playwright и..."
    })




