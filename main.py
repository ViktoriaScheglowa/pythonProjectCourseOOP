from src.file_handler_class import FileHandler
from src.hh_class import HH
from src.vacancies_class import Vacancy

if __name__ == '__main__':
    filename = "job_hh.json"
    hh = HH(filename)
    file_handler = FileHandler(filename)

    hh_vacancies = hh.load_vacancies("python")
    file_handler.write(hh.vacancies)

    for vacancies in hh.vacancies:
        vacancies_class = Vacancy.get_vacancy(vacancies)