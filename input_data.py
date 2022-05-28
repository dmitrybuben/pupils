def namesurname():
    print('Заполняем имя, фамилия')
    id = int(input('Введите уникальный номер ученика: '))
    name = input('Введите имя ученика: ')
    surname = input('Введите фамилию ученика: ')
    with open('table1.csv', 'a') as file:
        file.write(f'{id};{name};{surname}\n')
    print('Запись внесена')


def address():
    print('Запоняем адрес')
    id = int(input('Введите уникальный номер ученика: '))
    street = input('Введите название улицы: ')
    house = input('Введите номер дома: ')
    flat = input('Введите номер квартиры: ')
    with open('table2.csv', 'a') as file:
        file.write(f'{id};{street};{house};{flat}\n')
    print('Запись внесена')


def cabinet():
    print('Запоняем класс')
    id = int(input('Введите уникальный номер ученика: '))
    table = input('Введите номер парты: ')
    coulumn = input('Введите ряд: ')
    var = input('Введите номер варианта: ')
    with open('table3.csv', 'a') as file:
        file.write(f'{id};{table};{coulumn};{var}\n')
    print('Запись внесена')

# namesurname()
# address()
# cabinet()