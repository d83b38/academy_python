import csv


def read_csv_data(relative_url: str, encoding: str = 'utf8', delimiter: str = ';') -> list[dict]:
    """ Чтение csv файла """
    with open(relative_url, 'r', newline='', encoding=encoding) as csvfile:
        data_reader = csv.reader(csvfile, delimiter=delimiter)
        column_names = ['Индекс']  # в решении напрямую не использован, но коль делаем pandas на минималках он есть
        column_names.extend(next(data_reader))  # считываем первую строку с названием колонок
        rows_count = 0
        data = []

        for row in data_reader:
            indexed_row = [rows_count]
            indexed_row.extend(row)
            data.append({column_names[i]: indexed_row[i] for i in range(len(column_names))})
            rows_count += 1
    return data


def get_department_team_hierarchy(data: list[dict],
                                  department_column_name: str = 'Департамент',
                                  team_column_name: str = 'Отдел') -> dict:
    """
    Получить иерархию департамента и отдела в виде словаря
    {название департамента: спикок отделов}
    department - департамент, team - отдел
    """
    department_set = set()
    department_team_pair_list = []  # список кортежей пар департамент-отдел вида [(департамент, отдел)]
    department_team_hierarchy = {}  # {название департамента: спикок отделов}

    for row in data:
        department_set.add(row[department_column_name])
        department_team_pair_list.append((row[department_column_name], row[team_column_name]))

    for department in department_set:
        team_list = []
        for pair in set(department_team_pair_list):
            if pair[0] == department:
                team_list.append(pair[1])
        department_team_hierarchy[department] = team_list
    return department_team_hierarchy


def output_hierarchy(department_team_hierarchy: dict) -> None:
    """ Вывод в консоль словаря вида иерархии департамент-отдел """
    print('\nОтчет по иерархиям департаментов:')
    for department, team_list in department_team_hierarchy.items():
        print(department)
        for team in team_list:
            print(f'-> {team}')
    print('\n ')


def get_department_report(data: list[dict], department_column_name: str = 'Департамент') -> list[dict]:
    """ Получить отчет по департмаентам """
    department_set = set()
    department_report = []

    for row in data:
        department_set.add(row[department_column_name])

    for department in department_set:
        department_info_dict = {}
        emp_list = []
        for row in readed_data:
            if row[department_column_name] == department:
                emp_list.append(row)
        salary_list = [int(row['Оклад']) for row in emp_list]
        department_info_dict['Название'] = department
        department_info_dict['Численность'] = len(emp_list)
        department_info_dict['Мин. оклад'] = min(salary_list)
        department_info_dict['Макс. оклад'] = max(salary_list)
        department_info_dict['Ср. оклад'] = round(sum(salary_list) / len(emp_list))
        department_report.append(department_info_dict)
    return department_report


def output_department_report(department_report: list[dict]) -> None:
    """ Вывод в консоль отчет по департаментам """
    print('\nСводный отчет по департаментам:')
    for department_dict in department_report:
        department_info_string = ''
        for column_name, column_value in department_dict.items():
            department_info_string += f'{column_name}: {column_value}; '
        print(department_info_string)
    print('\n ')


def department_report_to_csv(department_report: list[dict],
                             relative_url: str,
                             encoding: str = 'utf8',
                             delimiter: str = ';') -> None:
    """ Сохранить отчет по департаментам в csv файл """
    column_names = department_report[0].keys()
    with open(relative_url, 'w', newline='', encoding=encoding) as output_file:
        data_writer = csv.DictWriter(output_file, column_names, delimiter=delimiter)
        data_writer.writeheader()
        data_writer.writerows(department_report)
    print(f'Файл успешно сохранен в директории проекта по адресу {relative_url} \n')


def menu(data: list[dict]) -> None:
    """ Ввод/вывод действий меню и исполнение команд"""
    option = ''
    options_map = {1: '1. Вывести иерархию департаментов и отделов',
                   2: '2. Вывести сводный отчёт по департаментам в консоль',
                   3: '3. Вывести сводный отчёт по департаментам в csv'}

    while option not in options_map:
        print('Выберите номер команды меню:')
        for value in options_map.values():
            print(value)
        try:
            option = int(input())
        except:
            option = ''

    match option:
        case 1:
            print(1)
            department_team_hierarchy = get_department_team_hierarchy(data)
            output_hierarchy(department_team_hierarchy)
        case 2:
            print(2)
            department_report = get_department_report(data)
            output_department_report(department_report)
        case 3:
            print(3)
            department_report = get_department_report(data)
            department_report_to_csv(department_report, 'homework_2/department_report.csv')
    menu(data)  # рекурсивный вызов функции для запроса новых команд


if __name__ == '__main__':
    readed_data = read_csv_data('homework_2/Corp_Summary.csv', encoding='utf8', delimiter=';')
    menu(readed_data)
