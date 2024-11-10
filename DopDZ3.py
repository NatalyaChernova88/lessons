list_s = [[1, 2, 3], {'a':4, 'b':5}, (6, {'cube':7, 'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def data_structure(element):
    count = 0
    if isinstance(element, (list, set, tuple)):
        for i in element:
            count += data_structure(i)
    elif isinstance(element, int):
        count += element
    elif isinstance(element, str):
        count += len(element)
    elif isinstance(element, dict):
        for key, value in element.items():
            count += data_structure(key)
            count += data_structure(value)
    return count

print(data_structure(list_s))