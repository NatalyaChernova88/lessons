first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first==second==third:
    print(3)
elif first==second or first==third or second==first or second==third or third==first or third==second:
    print(2)
elif first!=second or first!=third or second!=first or second!=third or third!=first or third!=second:
    print(0)