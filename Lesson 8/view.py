def action():
    print('Выберите действие')
    operation = int(input(' 1 - Запись\n 2 - Чтение\n 3 - Изменить\n 4 - Удалить\n 5 - Завершение программы\n'))
    return operation

def get_new_person():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    surname = input('Отчество: ')
    telephone = input ('Номер телефона: ')
    data_str = last_name + " " + first_name + " " + surname + " " + telephone + "\n"
    return data_str



