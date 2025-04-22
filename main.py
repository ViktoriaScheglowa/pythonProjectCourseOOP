from src.file_handler_class import FileHandler
from src.hh_class import HH, HhBase
from src.user_function import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies
from src.vacancies_class import Vacancy


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HH()
file_handler = FileHandler()


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.get_vacancy(hh_vacancies)
    file_handler.add_vacancy(vacancies_list)

    file_handler.del_vacancy(vacancies_list[0])
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
