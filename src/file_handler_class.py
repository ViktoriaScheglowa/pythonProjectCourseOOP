import json
import os.path
from abc import ABC, abstractmethod

from src.vacancies_class import Vacancy


class FileHandlerBase(ABC):
    """Абстрактный класс"""
    @abstractmethod
    def write(self, text: list) -> None:
        pass

    @abstractmethod
    def open_file(self) -> None:
        pass

    @abstractmethod
    def add_vacancy(self, list_vacancy_hh: list[Vacancy]) -> None:
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: Vacancy) -> None:
        pass


class FileHandler(FileHandlerBase):
    """Класс для работы с файлом"""
    __slots__ = ("filename", "data_file")

    def __init__(self, filename="job_hh.json"):
        self.filename = "./data/" + filename
        self.data_file = []

        self.open_file()

    def open_file(self) -> None:
        """Метод открытия файла"""
        if os.path.exists(self.filename):
            with open(self.filename, mode="r", encoding="utf-8") as file:
                self.data_file = json.load(file)
        else:
            with open(self.filename, mode="a", encoding="utf-8"):
                pass

    def write(self, text: list[dict]):
        """Метод записи в файл"""
        with open(self.filename, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(text, ensure_ascii=False, indent=4))
        self.data_file = text

    def add_vacancy(self, list_vacancy_hh: list[Vacancy]) -> None:
        """Метод добавления в файл новых вакансий"""
        list_vacancy = [vacancy.to_dict() for vacancy in list_vacancy_hh]
        self.write(list_vacancy)

    def del_vacancy(self, vacancy: Vacancy) -> None:
        """Метод удаления из файла вакансий"""
        for index, data in enumerate(self.data_file):
            if data["id_vacancy"] == vacancy.id_vacancy:
                print(data)
                del self.data_file[index]
                break
        self.write(self.data_file)
