from abc import ABC, abstractmethod
import requests


class HhBase(ABC):
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(HhBase):
    """
    Класс для работы с API HeadHunter
    Класс HhBase является родительским классом
    """

    def __init__(self, file_worker):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword) -> list:
        self.__params['text'] = keyword
        while self.__params.get('page') != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
        return self.__vacancies
