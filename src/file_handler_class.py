import json
import os.path
from abc import ABC, abstractmethod

from src.vacancies_class import Vacancy


class FileHandlerBase(ABC):
    """Абстрактный класс который перечисляет методы наследоваемых классов"""

    @abstractmethod
    def write(self, text: list[dict], file_mode: str) -> None: ...
    @abstractmethod
    def open_file(self) -> None: ...
    @abstractmethod
    def add_vacancy(self, list_vacancy_hh: list[Vacancy]) -> None: ...
    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None: ...


class FileHandler(FileHandlerBase):
    """Класс работы с файлом"""

    __slots__ = ("filename", "data_file")
    __filename: str
    data_file: list

    def __init__(self, filename: str = "job_hh.json"):
        self.__filename = "./data/" + filename
        self.data_file = []

        # Создаем файл если он не создан
        self.open_file()

    def open_file(self) -> None:
        """Метод открытия файла"""
        if os.path.exists(self.__filename):
            with open(self.__filename, mode="r", encoding="utf-8") as file:
                self.data_file = json.load(file)
        else:
            with open(self.__filename, mode="a", encoding="utf-8"):
                pass

    def write(self, text: list[dict], file_mode: str) -> None:
        """Запись в файл"""
        with open(self.__filename, mode=file_mode, encoding="utf-8") as file:
            file.write(json.dumps(text, ensure_ascii=False, indent=4))
        self.data_file = text

    def add_vacancy(self, list_vacancy_hh: list[Vacancy]) -> None:
        """Метод добавления в файл новых вакансий"""
        list_ids = [values["id_vacancy"] for values in self.data_file]
        list_vacancy = [vacancy.to_dict() for vacancy in list_vacancy_hh if vacancy.requirement not in list_ids]
        self.write(list_vacancy, "a")

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии"""
        for index, data in enumerate(self.data_file):
            if data["id_vacancy"] == vacancy.id_vacancy:
                del self.data_file[index]
                break
        self.write(self.data_file, "w")
