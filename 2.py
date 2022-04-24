def nevt(a, q):
    try:
        global w
        w = a/q
        return w
    except ZeroDivisionError:
        w = 0
        return w


a = int(input("введи первое число "))
q = int(input("введи второе число "))
nevt(a, q)
if w > 0:
    print(f"вот твое деление:{nevt(a, q)}")
else:
    print("Нелзя делить на ноль? ")
