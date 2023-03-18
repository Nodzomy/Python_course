def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def update_info(original: dict):
    print("Оставьте поле пустым, если не хотите его менять\n")
    info = {}
    inputStr = input('Введите фамилию: ')
    if inputStr != "":
        info['Фамилия'] = inputStr
    else:
        info['Фамилия'] = original.get("Фамилия")
   
    inputStr = input('Введите имя: ')
    if inputStr != "":
        info['Имя'] = inputStr
    else:
        info['Имя'] = original.get("Имя")
   
    inputStr = input('Введите номер телефона: ')
    if inputStr != "":
        info['Телефон'] = inputStr
    else:
        info['Телефон'] = original.get("Телефон")
   
    inputStr = input('Введите описание: ')
    if inputStr != "":
        info['Описание'] = inputStr
    else:
        info['Описание'] = original.get("Описание")
    
    return info

def writing_scv(info):
    file = 'Seminar8/Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_scv_list(data: list):
    with open("Seminar8/Phonebook.csv", "w", encoding='utf-8') as f:
        for info in data:
            f.write(f'{info.get("Фамилия")};{info.get("Имя")};{info.get("Телефон")};{info.get("Описание")}\n')

def read_csv(file: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(file, 'r', encoding='utf-8') as readFile:
        for line in readFile:
            record = dict(zip(fields, line.strip().split(';')))
            data.append(record)

    return data


def find_by_name(data: list, last_name: str):
    for info in data:
        if info.get("Фамилия") == last_name:
            print(f'\nНомер телефона: {info.get("Телефон")}')
            return info
    print("Такой абонент отсутствует")
    return None


def find_by_number(data: list, phone_number: str):
    for info in data:
        if info.get("Телефон") == phone_number:
            print(f'{info.get("Фамилия")}, {info.get("Имя")}')
            return info
    print("Такой абонент отсутствует")
    return None

def choice2(data: list, info: dict):
    selection = str(input("Хотите удалить или изменить запись? (да/нет) "))
    if selection == "да":
        print("\nВыберите необходимое действие:\n"
              "1. Удалить\n"
              "2. Редактировать\n")
        choice1 = int(input('\nВведите число: '))
        if choice1 == 2:
            newInfo = update_info(info)
            editing(data, info, newInfo)
        if choice1 == 1:
            del_row(data, info.get("Телефон"))


def editing(data: list, old_person: dict, new_person: dict):
    i = 0
    for info in data:
        if info.get("Фамилия") == old_person.get("Фамилия"):
            data[i] = new_person

        i += 1
    
    writing_scv_list(data)

def del_row(data:list, phone_number:str):
    i = 0
    for item in data:
        if item.get("Телефон") == phone_number:
            del data[i]
        
        i += 1
    
    writing_scv_list(data)