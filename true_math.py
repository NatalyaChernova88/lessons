from math import inf

def divide(first, second):
    if second == 0:
        return inf
    return first / second

print(divide(5,0))
print(divide(24,8))

if __name__ == '__main__':
    main()