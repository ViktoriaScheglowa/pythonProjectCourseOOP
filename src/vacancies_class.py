

class Vacancy:
    def __init__(self, name: str, url: str, salary: str, requirement: str):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        return f"{self.name} {self.url} {self.salary} {self.requirement}"

    @staticmethod
    def get_vacancy(dict_key):
        name = dict_key.get("name", "Нет названия")
        url = dict_key.get("url", "Нет url")
        requirement = dict_key.get("snippet", {}).get("requirement", "Нет requirement")
        salary = dict_key.get("salary", None)
        text_rub_salary = "Нет информации"

        if salary:
            salary_from = salary.get("from", 0)
            salary_to = salary.get("to", 0)
            salary_currency = "руб." if salary.get("currency", "") == "RUR" else ""
            text_rub_salary = f"{salary_from}{salary_currency} - {salary_to}{salary_currency}"

        return Vacancy(name, url, text_rub_salary, requirement)
     