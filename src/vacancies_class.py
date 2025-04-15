

class Vacancy:
    def __init__(self, name: str, url: str, salary: str, requirement: str):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        return f"{self.name} {self.url} {self.salary} {self.requirement}"

    @staticmethod
    def get-vacancy(dict_key):
        name = dict-key.get("name", "Нет названия")
        url = dict-key.get("url", "Нет url")
        requirement = dict-key.get("snippet", {}).get("requirement", "Нет requirement")
        salary = dict-key.get("salary", None)
        text_rub_salary = "Нет информации"

    if salary:
        salary_from = salary.get("from", 0)
        salary_to = salary.get("to", 0)
        salary_currency = "руб." if salary.get("currency", "") == "RUR" else ""
        text_rub_salary = f"{salary_from}{salary_currency} - {salary_to}{salary_currency}"

     return Vacancy(name, url, text_rub_salary, requirement)