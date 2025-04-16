
class Vacancy:
    def __init__(self, name: str, url: str, salary: str, requirement: str):
        self.name = name
        self.url = url
        self.salary = salary
        self.salary_from = 0
        self.salary_to = 0
        self.requirement = requirement

    def __str__(self):
        return f"{self.name} {self.url} {self.salary} {self.requirement}"

    @staticmethod
    def get_vacancy(list_hh_vacancy: list) -> list['Vacancy']:
        list_vacancy = []

        for dict_key in list_hh_vacancy:
            name = dict_key.get("name", "Нет названия")
            url = dict_key.get("url", "Нет url")
            requirement = dict_key.get("snippet", {}).get("requirement", "Нет requirement")

            salary = dict_key["salary"]
            price_from = salary["from"] if salary and salary["from"] else 0
            price_to = salary["to"] if salary and salary["to"] else 0

            list_vacancy.append(Vacancy(name, url, price_from, price_to, requirement))
        return list_vacancy

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement
        }
