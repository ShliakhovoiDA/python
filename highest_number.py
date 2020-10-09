numeral = int(input("Введите любое целое положительное число: "))
last_number = numeral % 10
numeral = numeral // 10
while numeral > 0:
    if numeral % 10 > last_number:
        last_number = numeral % 10
    numeral = numeral // 10
print(last_number)