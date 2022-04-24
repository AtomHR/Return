def q(i, k):
    global p
    p = i + k
    return p


r = int(input("введи число "))
w = int(input("введи число "))
e = int(input("введи число "))


if r > w > e:
    i = r
    k = w
    print(f"сумма двух больших чисел {q(i, k)}")
elif r > e > w:
    i = r
    k = e
    print(f"сумма двух больших чисел {q(i, k)}")

elif w > e > r:
    i = w
    k = e
    print(f"сумма двух больших чисел {q(i, k)}")
elif w > r > e:
    i = w
    k = r
    print(f"сумма двух больших чисел {q(i, k)}")

elif e > r > w:
    i = e
    k = r
    print(f"сумма двух больших чисел {q(i, k)}")

elif e > w > r:
    i = e
    k = w
    print(f"сумма двух больших чисел {q(i, k)}")
