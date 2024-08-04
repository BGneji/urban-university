# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
import inspect


def introspection_info(obj):
    d = {}
    d["type"] = type(obj).__name__
    d['attributes'] = dir(obj)
    d['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    def get_module_name(function):
        module = inspect.getmodule(function)
        if module is not None:
            return module.__name__
        else:
            return None

    module_name = get_module_name(introspection_info)
    d['module'] = module_name
    return d


if __name__ == "__main__":
    number_info = introspection_info(42)
    print(number_info)
