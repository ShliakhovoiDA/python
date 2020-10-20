month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
              9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

month_deutsch = {1: 'Januar', 2: 'Februar', 3: 'März', 4: 'April', 5: 'Mai', 6: 'Juni', 7: 'Juli', 8: 'August',
                 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Dezember'}

month_list = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август',
              'сентябрь', 'октябрь', 'ноябрь', 'декабрь')


def season():
    if month == 12 or month <= 2:
        print(f'Месяц {month_dict[month]} - это зима, по-немецки Winter.')
    elif 3 <= month <= 5:
        print(f'Месяц {month_dict[month]} - это весна, по-немецки Frühling.')
    elif 6 <= month <= 8:
        print(f'Месяц {month_dict[month]} - это лето, по-немецки Sommer.')
    elif 9 <= month <= 11:
        print(f'Месяц {month_dict[month]} - это осень, по-немецки Herbst.')


# пока не понимаю, как избавиться от    None при выводе данных

while True:
    month = int(input('Введите месяц цифрой от 1 до 12, и узнаете как он называется по-русски и по-немецки,'
                      ' и к какому времени года он относится: '))
    if 1 <= month <= 12 and month in month_dict:
        print(f'{month}-й месяц назвается {month_dict[month]}, а по-немецки это {month_deutsch[month]}.')
        print(
            f'В реализации через список: {month}-й месяц назвается {month_list[month - 1]}, а по-немецки это {month_deutsch[month]}.')
        print(f'{season()}')
        break
    else:
        print('Необходимо ввести месяц цифрой, от 1 до 12, и только. Попробуйте еще разок :) ')
        continue
