from datetime import datetime


def get_log(func):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('decoratorlogs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n')
        return result
    return foo


@get_log
def get_generator(list_of_lists):
    for sub_list in list_of_lists:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':
    get_generator('my_generator.txt')