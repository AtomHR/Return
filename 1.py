a = int(input("какое количество километров вы пробежали? "))
b = int(input(f"а какое количество километров вы хотите пробежать? "))
q = 1

while a < b:
    if a < b:
        print(f"день {q}, вы пробежали {a} километров, ваша цель {b} километров")
        a += a * 0.1
        a = round(a, 2)
        q += 1

a += a * 0.1
a = round(a, 2)
q += 1
print(f"день {q}, вы пробежали {a} километров, ваша цель была пробежать не менее {b} километров")
