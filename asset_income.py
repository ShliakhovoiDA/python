income = float(input("Введите сумму выручки в рублях: "))
charges = float(input("Введите сумму расходов в рублях: "))
if charges > income:
    print("Ваши расходы превышают доходы, Вам нужно что-то изменить.")
elif charges == income:
    print("Ваши доходы равны расходам. Наверное, это не очень хорошо.")
elif charges < income:
    print("Ваши доходы превышают расходы, так держать!")
    personal = int(input("Введите количество сотрудников: "))
    gain_per_person = (income - charges) / personal
    print(f'Прибыль в расчете на сотрудника составляет {gain_per_person:.2f} рублей')