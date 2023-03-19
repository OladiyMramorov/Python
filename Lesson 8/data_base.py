import view
def add_person():
    with open('file.txt', 'a', encoding='UTF-8') as data:
        data.write(view.get_new_person())


def find_person():
    input_str = input('Введите искомый параметр (Фамилия, Имя, Отчество или Телефон): ')
    with open('file.txt', 'r', encoding='UTF-8') as data:
        for i in data.readlines():
            if input_str in i:
                print(i.strip())

def change_person():
    input_str = input('Введите изменяемый параметр (Фамилия, Имя, Отчество или Телефон): ')
    user_list = []
    with open('file.txt', 'r', encoding='UTF-8') as data:
        lst = data.readlines()
        for line in lst:
            if input_str in line:
                user_list.append(line)
    print(*user_list)
    answer = int(input('Введите стоку для изминения: '))
    print('Введите новый параметр')
    new_str = view.get_new_person()
    with open('file.txt', 'w', encoding='UTF-8') as data:
        for line in lst:
            if user_list[answer-1] != line:
                data.write(line)
            else:
                data.write(new_str)
    print('Изменено')

def delete_data():
    input_str = input('Введите параметр для удаления строки: ')
    user_list = []
    with open('file.txt', 'r', encoding='UTF-8') as data:
        lst = data.readlines()
        for line in lst:
            if input_str in line:
                user_list.append(line)
    print(*user_list)
    answer = int(input('Введите стоку для удаления: '))
    with open('file.txt', 'w', encoding='UTF-8') as data:
        for line in lst:
            if user_list[answer-1] != line:
                data.write(line)
            else:
                continue
    print('Удалено')