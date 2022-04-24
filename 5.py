'''def my_func(x, y):
    return -(x ** y)


x = abs(int(input('Введи число x: ')))
y = abs(int(input('Введи число y: ')))


print(my_func(x, y))
'''

q = 2


def my_func(x, y):
    global q

    if x <= 0:
        return print("Нет, х должен быть больше нуля")

    if y >= 0:
        return print("Нет, y должен быть меньше нуля")

    y = abs(y)
    while q <= y:
        x *= w
        q += 1

    if q == (y + 1):
        return -x


x = int(input('Введи число x: '))
y = int(input('Введи число y: '))
w = x
print(my_func(x, y))
