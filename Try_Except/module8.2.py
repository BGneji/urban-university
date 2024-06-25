class ProcessingException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


def res(a,  b):
    if isinstance(b, str):
        raise ProcessingException(f'Аргумент b имеет тип строка', f'b не должен быть строкой ')
    elif isinstance(a, int):
        raise ProcessingException(f'Аргумент a имеет тип int', f'a не должен иметь тип int ')
    return int(a) + b


try:

    print(res(1, '2'))

except ProcessingException as e:
    print("Словили ошибки")
    print(e.message)
    print(e.info)

print(f'Программа отработала как надо ответ: {res("1", 2)}')