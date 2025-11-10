def fibonacci1(n):
    (a, b) = (0, 1)
    # a = 0
    # b = 1

    for _ in range(n):
        (a, b) = (b, a + b)
        # tp = (b, a + b)
        # a = tp[0]
        # b = tp[1]
        # a = b
        # b = a + b

    return a


def fibonacci2(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        new = fib[i - 1] + fib[i - 2]
        fib.append(new)
        print(fib)

    return fib[n]


print(f"F0: {fibonacci1(0)}")
print(f"F1: {fibonacci1(1)}")
print(f"F2: {fibonacci1(2)}")
print(f"F3: {fibonacci1(3)}")
print(f"F9: {fibonacci1(9)}")

print("\n\n")

print(f"F0: {fibonacci2(0)}")
print(f"F1: {fibonacci2(1)}")
print(f"F2: {fibonacci2(2)}")
print(f"F3: {fibonacci2(3)}")
print(f"F9: {fibonacci2(9)}")
