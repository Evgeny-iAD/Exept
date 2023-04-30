try:
    s = input("Введите строку: ")
    if not s:
        raise Exception("Пустые строки вводить нельзя!")
except Exception as e:
    print("Ошибка: ", e)