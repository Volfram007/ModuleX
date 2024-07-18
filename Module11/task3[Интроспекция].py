import inspect


def introspection_info(obj):
    obj_info = {}

    # Тип объекта
    obj_info["type"] = type(obj)

    # Атрибуты объекта
    obj_info["attributes"] = [a for a in dir(obj) if not a.startswith('__') and not inspect.ismethod(getattr(obj, a))]

    # Методы объекта
    obj_info["methods"] = [m for m in dir(obj) if not m.startswith('__') and inspect.ismethod(getattr(obj, m))]

    # Модуль, к которому объект принадлежит
    obj_info["module"] = inspect.getmodule(obj)

    # Другие интересные свойства объекта
    if inspect.isfunction(obj) or inspect.ismethod(obj):
        obj_info["arguments"] = inspect.getfullargspec(obj).args

    return obj_info


number_info = introspection_info([4, 6])
print(number_info)
