# Переписал решение, но разобрался до полного понимания. Большой дефицит времени.

goods = []
options = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analysis = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
number = 0

while True:
    if input('Для выхода нажмите "Q" - Для продолжения нажмите "Enter"').upper() == 'Q':
        break
    number += 1
    for i in options.keys():
        description = input(f'Введите значение свойства товара "{i}": ')
        options[i] = int(description) if (i == 'цена' or i == 'количество') else description
        analysis[i].append(options[i])
    goods.append((number, options))
    print(f'\nСтруктура товаров\n{goods}')
    print(f'\nТекущая аналитика по товарам: \n {"*" * 40}')
    for key, value in analysis.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 40)
