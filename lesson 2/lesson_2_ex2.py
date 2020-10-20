my_list = list(input("Введите числа без пробелов: "))
print(f'Длина списка составляет {len(my_list)} цифр.')

for n in range(1, len(my_list), 2):
    my_list[n - 1], my_list[n] = my_list[n], my_list[n - 1]

print(f'Новый список имеет следующий вид: {my_list}')
