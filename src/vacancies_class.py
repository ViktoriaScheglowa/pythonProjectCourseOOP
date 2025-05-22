from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Абстрактный класс"""

    @staticmethod
    @abstractmethod
    def create_vacancies(list_hh_vacancy: list) -> list["Vacancy"]: ...
    @abstractmethod
    def to_dict(self) -> dict: ...


class Vacancy(BaseVacancy):
    """Шаблон класса Вакансия"""

    __slots__ = ("id_vacancy", "name", "url", "salary_from", "salary_to", "requirement", "company_id")
    id_vacancy: str
    company_id: int
    name: str
    url: str
    salary_from: float
    salary_to: float
    requirement: str

    def __init__(
        self,
        id_vacancy: str,
        name: str,
        company_id: int,
        company_name: str,
        url: str,
        salary_from: float,
        salary_to: float,
        requirement: str,
    ):
        self.id_vacancy = self.__validate_id_vacancy(id_vacancy)
        self.company_id = self.__validate_company_id(company_id)
        self.name = self.__validate_name(name)
        self.company_name = self.__validate_company_name(company_name)
        self.url = self.__validate_site_url(url)
        self.salary_from = self.__validate_salary_from(salary_from)
        self.salary_to = self.__validate_salary_to(salary_to)
        self.requirement = self.__validate_requirement(requirement)

    def __repr__(self) -> str:
        """Переопределение магического метода"""
        return str(self.to_dict())

    def __lt__(self, other: "Vacancy") -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_to < other.salary_to

    @staticmethod
    def __validate_id_vacancy(id_vacancy: str) -> str:
        """Валидация аттрибута "ID" в вакансии"""
        if not isinstance(id_vacancy, str) or not id_vacancy:
            return "ID не указан"
        return id_vacancy

    @staticmethod
    def __validate_company_id(company_id: int) -> int:
        """Валидация аттрибута "company_id" в вакансии"""
        if isinstance(company_id, int):
            return company_id
        raise ValueError("Компания не найдена")

    @staticmethod
    def __validate_name(name: str) -> str:
        """Валидация аттрибута "названия" в вакансии"""
        if not isinstance(name, str) or not name:
            return "Название не указано"
        return name

    @staticmethod
    def __validate_company_name(company_name: str) -> str:
        """Валидация аттрибута "названия" в вакансии"""
        if isinstance(company_name, str) or company_name:
            return company_name
        raise ValueError("Название компании не указано")

    @staticmethod
    def __validate_requirement(requirement: str) -> str:
        """Метод для валидации работодателя"""
        if not isinstance(requirement, str) or not requirement:
            return "Краткое описание не указано"
        return requirement

    @staticmethod
    def __validate_salary_from(salary_from: int | float) -> int | float:
        """Валидация заработной платы ОТ"""
        if not isinstance(salary_from, (int, float)) or salary_from < 0:
            return 0
        return salary_from

    @staticmethod
    def __validate_salary_to(salary_to: int | float) -> int | float:
        """Валидация заработной платы ДО"""
        if not isinstance(salary_to, (int, float)) or salary_to < 0:
            return 0
        return salary_to

    @staticmethod
    def __validate_site_url(url: str) -> str:
        """Метод для валидации ссылки на вакансию"""
        if not isinstance(url, str) or not url.startswith("http"):
            return "URL не указан"
        return url

    @classmethod
    def create_vacancies(cls, list_hh_vacancy: list) -> list["Vacancy"]:
        """Получение вакансий в виде списка"""
        list_vacancy = []
        for dict_key in list_hh_vacancy:
            id_vacancy = dict_key["id"]
            employer = dict_key["employer"]
            name = dict_key.get("name", "Нет названия")
            url = dict_key.get("url", "Нет url")

            company_name = employer["name"]
            company_id = int(employer["id"])

            get_snippet = dict_key["snippet"]
            chk_snippet = get_snippet if get_snippet else None
            get_requirement = chk_snippet["requirement"] if chk_snippet else None
            requirement = get_requirement if get_requirement else "Нет requirement"

            salary = dict_key["salary"]
            price_from = salary["from"] if salary and salary["from"] else 0
            price_to = salary["to"] if salary and salary["to"] else 0

            list_vacancy.append(
                cls(id_vacancy, name, company_id, company_name, url, price_from, price_to, requirement)
            )
        return list_vacancy

    def to_dict(self) -> dict:
        """Изменение формата вывода вакансии"""
        return {
            "id_vacancy": self.id_vacancy,
            "name": self.name,
            "url": self.url,
            "company_name": self.company_name,
            "company_id": self.company_id,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement,
        }
