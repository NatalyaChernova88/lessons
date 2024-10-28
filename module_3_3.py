# def print_params(a = 1, b = 'строка', c = True):
#     print(a, b, c)
# values_list = [5, 'hello', False]
# values_dict = {'a' : 3, 'b' : 'ks', 'c' : 6}
# values_list_2 = [54.32, "'Строка'"]
# print_params(b = 25)
# print_params(c = [1, 2, 3])
                                # 1. ПАРАМЕТРЫ РАБОТАЮТ

# print_params(*values_list)
# print_params(**values_dict)
                                # 2. РАСПАКОВАЛА СПИСОК И СЛОВАРЬ
# print_params(*values_list_2, 42)
                                # 3. РАБОТАЕТ
def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)
append_to_list(4, 4)                #ВОТ ЭТО Я НЕ ПОНЯЛА СОВСЕМ.
                                                # У МЕНЯ ПОЛУЧАЕТСЯ ПУСТОЕ ПОЛЕ


