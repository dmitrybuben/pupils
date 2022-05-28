def findattr():
    f_id = input('Введите id ученика: ')
    with open('table1.csv', 'r') as file:
        list1 = [row.replace(';','').strip() for row in file]
        print(f'Фамилия, имя: {list1[int(f_id)-1]}')

    with open('table2.csv', 'r') as f:
        list2 = [row.replace(';','').strip() for row in f]
        print(f'Адрес: {list2[int(f_id)-1]}')

    with open('table3.csv', 'r') as f:
        list3 = [row.replace(';','').strip() for row in f]
        print(f'Класс: {list3[int(f_id)-1]}')