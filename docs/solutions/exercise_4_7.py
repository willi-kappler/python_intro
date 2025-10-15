def fibonacci(n):
     a, b = 0, 1

     for _ in range(n):
         a, b, = b, a + b

     return a

print(f"F0: {fibonacci(0)}")
print(f"F1: {fibonacci(1)}")
print(f"F2: {fibonacci(2)}")
print(f"F3: {fibonacci(3)}")
print(f"F9: {fibonacci(9)}")
