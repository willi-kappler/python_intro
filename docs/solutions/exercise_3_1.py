import numpy as np

a = np.arange(1, 10)
for i in range(a.size):
    if a[i] % 2 != 0:
        a[i] += 1

    print(a[i])
