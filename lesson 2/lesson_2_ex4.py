user_string = input('Введите несколько слов, разделенных пробелами: ').split()

for ind, el in enumerate(user_string, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, (el[:10]))
