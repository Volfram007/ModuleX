# from time import perf_counter


# def speedTestTimes(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Время начала работы программы
#
#         result = func(*args, **kwargs)
#
#         end_time = time.time()  # Время начала работы программы# Время окончания работы программы
#         elapsed_time = round(end_time - start_time, 4)  # Время работы программы
#         print(f"Время выполнения: {elapsed_time}сек. {func}")  # Время выполнения
#         return result
#
#     return wrapper


# def speedTest(func):
#     def wrapper(*args, **kwargs):
#         start_time = perf_counter()  # Время начала работы программы
#
#         result = func(*args, **kwargs)
#
#         end_time = perf_counter()  # Время окончания работы программы
#         elapsed_time = end_time - start_time  # Время работы программы
#         print(f"Время выполнения: {elapsed_time} {func}")  # Время выполнения
#         return result
#
#     return wrapper
