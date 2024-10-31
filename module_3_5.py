def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

# print(get_miltiplied_digits(123))                 #не понимаю почему ЭТО не работет
result = get_multiplied_digits(512)                 #а ЭТО работет
print(result)

# и не могу убрать нули. Происходит умножение на второй ноль и ошибка.
# разобрать бы на вебинаре