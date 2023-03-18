from os.path import exists
from scv_creating import creating
from file_writing import writing_scv, get_info, find_by_name, find_by_number, read_csv, choice2
from export import from_file


def view(data: list):
    for info in data:
        print(f'Фамилия: {info.get("Фамилия")}\nИмя: {info.get("Имя")}\nТелефон: {info.get("Телефон")}\nОписание: {info.get("Описание")}\n\n')

def record_info():
    info = get_info()
    writing_scv(info)

def choice():
    flag = input('\n Для продолжения работы нажмите \'да\', или 5 для завершения работы... ')
    while (flag.lower() == 'да'):
        path = 'Seminar8/Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()

        csv_data = read_csv(path)

        print("\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Закончить работу")
        choice_action = int(input('\nВведите число: '))
        if choice_action == 1:
            print("\n")
            view(csv_data)
        elif choice_action == 2:
            name = str(input("Введите фамилию: "))
            info = find_by_name(csv_data,name)
            if info is not None:            
                choice2(csv_data, info)
        elif choice_action == 3:
            phone = str(input("Введите телефон: "))
            info = find_by_number(csv_data,phone)
            if info is not None:            
                choice2(csv_data, info)
        elif choice_action == 4:
            record_info()
        elif choice_action == 5:
            print('Программа завершена.')
            break
    
