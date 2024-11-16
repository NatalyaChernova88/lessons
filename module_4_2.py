def test_function(name):
    def inner_function ():
        inner_function('Я в области видимости функции test_function')
    print(inner_function)
test_function(', чувак')
# print(inner_function('Я в области видимости функции test_function'))
# Выходит ошибка - name 'inner_function' is not defined. Did you mean: 'test_function'?
print(test_function)