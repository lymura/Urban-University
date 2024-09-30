import inspect


def introspection_info(obj):
    # Определение типа объекта
    type_name = type(obj).__name__

    # Определение атрибутов объекта
    attributes = dir(obj)

    # Определение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Определение модуля, к которому принадлежит объект
    module = inspect.getmodule(obj)

    # Формирование словаря с информацией об объекте
    introspection_data = {
        'type': type_name,
        'attributes': attributes,
        'methods': methods,
        'module': module.__name__ if hasattr(module, '__name__') else '<unknown>'
    }

    return introspection_data


class MyClass:
    def __init__(self):
        self.my_attribute = 'Some value'
        self.my_method = lambda x: x + 1

instance = MyClass()

number_info = introspection_info(42)
print(number_info)

object_info = introspection_info(instance)
print(object_info)