my_list = [6, 5, 3, 2, 2]

while True:
    new_el_int = input('Введите натуральное число для его оценки в нашем рейтинге:\nДля выхода введите "Quit".')
    if new_el_int.isdigit() and new_el_int != 'Quit':
        new_el_int = int(new_el_int)
        i = 0
        for el in my_list:
            if new_el_int <= el:
                i += 1
        my_list.insert(i, new_el_int)
        print(my_list)
        continue
    elif new_el_int == 'Quit':
        break
    else:
        # new_el_int != float(new_el_int) or not new_el_int.isdigit():
        print('Нужно ввести натуральное число! Попробуйте еще раз!')
        continue
