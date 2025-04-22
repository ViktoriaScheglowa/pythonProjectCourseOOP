class Vacancy():
    __slots__ = ("id_vacancy", "name", "url", "salary_from", "salary_to", "requirement")

    def __init__(self, id_vacancy: str, name: str, url: str, salary_from: float, salary_to: float, requirement: str):
        self.id_vacancy = id_vacancy
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    def __str__(self):
        """Магический метод для строкового отображения объекта"""
        return f"{self.id_vacancy}{self.name} {self.url} {self.salary_from} {self.salary_to} {self.requirement}"

    @staticmethod
    def get_vacancy(list_hh_vacancy: list) -> list['Vacancy']:
        """Получение вакансий в виде списка"""
        list_vacancy = []
        for dict_key in list_hh_vacancy:
            id_vacancy = dict_key["id"]
            name = dict_key.get("name", "Нет названия")
            url = dict_key.get("url", "Нет url")
            requirement = dict_key.get("snippet", {}).get("requirement", "Нет requirement")

            salary = dict_key["salary"]
            price_from = salary["from"] if salary and salary["from"] else 0
            price_to = salary["to"] if salary and salary["to"] else 0

            list_vacancy.append(Vacancy(id_vacancy, name, url, price_from, price_to, requirement))
        return list_vacancy

    def to_dict(self) -> dict:
        """Шаблон вывода вакансий"""
        return {
            "id_vacancy": self.id_vacancy,
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement
        }
