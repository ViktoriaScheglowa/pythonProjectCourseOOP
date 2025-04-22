import re
from src.vacancies_class import Vacancy


def filter_vacancies(vacancy_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Функция фильтрации данных"""
    return [vacancy_data
            for vacancy_data in vacancy_list
            for find_text in filter_words
            if re.search(find_text, vacancy_data.name, re.I)]


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Функция получения данных по размеру заработной платы"""
    salary_from, salary_to = [salary.strip() for salary in salary_range.split('-')]
    list_result = []
    for vacancy_data in filtered_vacancies:
        if float(salary_from) >= vacancy_data.salary_from and float(salary_to) <= vacancy_data.salary_to:
            list_result.append(vacancy_data)
    return list_result


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
    """Функция сортировки данных по размеру заработной платы"""
    return sorted(ranged_vacancies, key=lambda v: v.salary_to)


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Функция вывода данных по размеру заработной платы"""
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies) -> None:
    """Функция вывода данных по размеру заработной платы в консоль"""
    for top_v in top_vacancies:
        print(top_v)
