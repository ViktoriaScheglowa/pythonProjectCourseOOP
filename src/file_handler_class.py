import json
from abc import ABC, abstractmethod

from src.vacancies_class import Vacancy


class FileHandlerBase(ABC):

    @abstractmethod
    def write(self, text: list) -> None:
        pass


class FileHandler(FileHandlerBase):
    def __init__(self, filename="job_hh.json", mode="a"):
        self.filename = filename
        self.open_file = open("./data/" + self.filename, mode=mode, encoding="utf-8")

    def write(self, text: list) -> None:
        with self.open_file as file:
            file.write(json.dumps(text, ensure_ascii=False))

    def add_vacancy(self, list_vacancy_hh: list[Vacancy]) -> None:
        list_vacancy = [vacancy.to_dict() for vacancy in list_vacancy_hh]
        with self.open_file as file:
            file.write(json.dumps(list_vacancy, ensure_ascii=False, indent=4))

    def del_vacancy(self, list_vacancy_hh: list[Vacancy]) -> None:
        list_vacancy = [vacancy.to_dict() for vacancy in list_vacancy_hh]
        with self.open_file as file:
            file.write(json.dumps(list_vacancy, ensure_ascii=False))

