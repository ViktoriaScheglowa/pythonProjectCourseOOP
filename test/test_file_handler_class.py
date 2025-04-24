from src.file_handler_class import FileHandler
from src.vacancies_class import Vacancy


def test_file_handler(init_file_handler: FileHandler, init_vacancy: Vacancy):
    init_file_handler.write([init_vacancy.to_dict()], "a")
    init_file_handler.del_vacancy(init_vacancy)
    init_file_handler.add_vacancy([init_vacancy])
