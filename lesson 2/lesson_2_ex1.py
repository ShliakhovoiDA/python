my_list = [4, 45.56, "*" * 10, abs(-67.82), "joke", bin(56), EnvironmentError(), globals(), {12 + 1, 65.6}, False,
           int("35"), frozenset(), None]
print(f'Длина списка составляет {len(my_list)} элементов')
i = 0
while i < len(my_list):
    print(f'Элемент № {i + 1} в списке имеет {type(my_list[i])}')
    i += 1
