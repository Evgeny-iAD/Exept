import datetime
current_date = datetime.datetime.now()

def divide_by_zero():
    x = 1 / 0
    return x

def index_error():
    my_list = [1, 2, 3]
    x = my_list[3]
    return x

def value_error():
    x = int("hello")
    return x

try:
    divide_by_zero()
except ZeroDivisionError:
    print("Ошибка деления на ноль", current_date.strftime("%d.%m.%Y"))

try:
    index_error()
except IndexError:
    print("Выход за пределы списка", current_date.strftime("%d.%m.%Y"))

try:
    value_error()
except ValueError:
    print("Ошибка преобразования типов данных", current_date.strftime("%d.%m.%Y"))
