print("Данная программа поможет возвести некое положительное число Х в отрицательную степень У. Попробуйте!")


def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x > 0 and 0 > y:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения X в степень Y = {round(result, 8)}'
        else:
            return "Не соблюдены условия: Х - любое действительное число больше 0, а Y - любое целое отрицательное " \
                   "число \n Попробуйте еще раз!"
    except ValueError:
        return "Необходимо вводить числа!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


while True:
    print("Для выхода из программы введите 'q' для Х и для Y.\n ")
    n1 = input("Введите действительное положительное число Х: \n")
    n2 = input("Введите целое отрицательное число Y: \n")
    if n1 == "q" and n2 == "q":
        print("До свидания!")
        break
    elif n2 == "0":
        print("Отрицательная степень не может быть нулевой. На ноль делить нельзя!")
        continue
    else:
        print(my_func(n1, n2))