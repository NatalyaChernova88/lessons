def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second



if __name__ == '__main__':
    print(divide(5, 0))
    print(divide(15, 3))