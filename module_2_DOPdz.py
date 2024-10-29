import random
n = random.randint(3, 20)
string = ''
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            string += str(i)
            string += str(j)
print(n, string)
