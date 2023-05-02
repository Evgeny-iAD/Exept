import re

class InvalidDataException(Exception):
    pass

class FileWriterException(Exception):
    pass

def validate_data(data):
    fields = data.split()
    if len(fields) != 6:
        raise InvalidDataException("Недопустимое количество полей")
    surname, name, patronymic, birth_date, phone_number, gender = fields
    if not re.match(r"^[a-zA-Zа-яА-ЯёЁ]+$", surname+name+patronymic):
        raise InvalidDataException("Недопустимый формат имени")
    if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", birth_date):
        raise InvalidDataException("Неверный формат даты рождения")
    if not re.match(r"^\d+$", phone_number):
        raise InvalidDataException("Неверный формат телефонного номера")
    if gender not in ["f", "m"]:
        raise InvalidDataException("Недопустимое значение пола")
    return fields

def save_data(fields):
    filename = fields[0] + ".txt"
    with open(filename, "a") as f:
        f.write(" ".join(fields) + "\n")

if __name__ == "__main__":
    data = input("Введите данные (surname name patronymic birth_date phone_number gender): ")
    try:
        fields = validate_data(data)
        save_data(fields)
    except InvalidDataException as e:
        print("Неверный формат данных:", e)
    except FileWriterException as e:
        print("Ошибка записи файла:", e)
    except Exception as e:
        print("Неизвестная ошибка:", e)
