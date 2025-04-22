import os

from src.file_handler_class import FileHandler
from src.vacancies_class import Vacancy


def test_file_handler(init_file_handler: FileHandler, init_vacancy: Vacancy):
    assert os.path.exists(init_file_handler.filename) == True

    init_file_handler.write([init_vacancy.to_dict()])
    init_file_handler.del_vacancy(init_vacancy)
    init_file_handler.add_vacancy([init_vacancy])
