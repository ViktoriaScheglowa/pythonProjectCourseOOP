import pytest

from src.file_handler_class import FileHandler
from src.hh_class import HH
from src.vacancies_class import Vacancy


@pytest.fixture
def vacancy_data() -> dict:
    return {
        "id": "119337028",
        "premium": False,
        "name": "Backend-разработчик",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "2", "name": "Санкт-Петербург", "url": "https://api.hh.ru/areas/2"},
        "salary": {"from": 100000, "to": 170000, "currency": "RUR", "gross": False},
        "salary_range": {
            "from": 100000,
            "to": 170000,
            "currency": "RUR",
            "gross": False,
            "mode": {"id": "MONTH", "name": "За\xa0месяц"},
            "frequency": None,
        },
        "type": {"id": "open", "name": "Открытая"},
        "address": {
            "city": "Санкт-Петербург",
            "street": "Фурштатская улица",
            "building": "24",
            "lat": 59.945472,
            "lng": 30.355187,
            "description": None,
            "raw": "Санкт-Петербург, Фурштатская улица, 24",
            "metro": None,
            "metro_stations": [],
            "id": "14978221",
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2025-04-09T15:10:44+0300",
        "created_at": "2025-04-09T15:10:44+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=119337028",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/119337028?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/119337028",
        "relations": [],
        "employer": {
            "id": "10711309",
            "name": "Системы планирования производства и логистики",
            "url": "https://api.hh.ru/employers/10711309",
            "alternate_url": "https://hh.ru/employer/10711309",
            "logo_urls": {
                "original": "https://img.hhcdn.ru/employer-logo-original/1220919.png",
                "90": "https://img.hhcdn.ru/employer-logo/6504117.png",
                "240": "https://img.hhcdn.ru/employer-logo/6504118.png",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10711309",
            "accredited_it_employer": False,
            "employer_rating": None,
            "trusted": True,
        },
        "snippet": {
            "requirement": None,
            "responsibility": "Backend разработка и доработка решения. Стек: <highlighttext>Python</highlighttext>: "
            "Django(DRF), PostgreSQL. Code review. Взаимодействие с командой разработки.",
        },
        "show_contacts": True,
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "fly_in_fly_out_duration": [],
        "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
        "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
        "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
        "night_shifts": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "employment_form": {"id": "FULL", "name": "Полная"},
        "internship": False,
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }


@pytest.fixture
def init_hh() -> HH:
    return HH()


@pytest.fixture
def init_file_handler() -> FileHandler:
    return FileHandler()


@pytest.fixture
def init_vacancy() -> Vacancy:
    return Vacancy(
        id_vacancy="119602010",
        name="Тестировщик (QA-инженер)",
        url="https://api.hh.ru/vacancies/119602010?host=hh.ru",
        salary_from=1,
        salary_to=10000,
        requirement="Знакомство с Postman и умение составлять API запросы. Знание основ HTML, CSS, JS, "
        "<highlighttext>Python</highlighttext>. Опыт написания тестовой документации "
        "(тест-кейсы...",
    )
