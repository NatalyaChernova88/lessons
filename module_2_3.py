my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
n = my_list[index]
while n >= 0 and index < len(my_list):
    n = my_list[index]
    index = index + 1
    if n < 0:
        break
    elif n == 0:
        continue
    else:
        print(n)





