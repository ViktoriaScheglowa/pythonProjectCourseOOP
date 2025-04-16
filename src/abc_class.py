from abc import ABC, abstractmethod


class Parser():
    def __init__(self, file_worker):
        self.file_worker = file_worker

    def load_vacancies(self, keyword):
        pass
