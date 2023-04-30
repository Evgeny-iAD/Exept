def get_float_input():
    while True:
        try:
            user_input = float(input("Введите дробное число: "))
            return user_input
        except ValueError:
            print("Ошибка: неправильный формат числа. Попробуйте снова.")


num = get_float_input()
print("Вы ввели число:", num)