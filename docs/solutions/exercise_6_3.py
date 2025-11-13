import numpy as np
import matplotlib.pyplot as plt
import random


def ant_model(width, height, num_iter):
    if width < 5:
        raise ValueError(f"Width must be at least 5: {width}")

    if height < 5:
        raise ValueError(f"Height must be at least 5: {height}")

    # Random start position:
    x = random.randint(1, width - 2)
    y = random.randint(1, height - 2)

    # Random direction at the beginning:
    # 0 = up
    # 1 = right
    # 2 = down
    # 3 = left
    d = random.randint(0, 3)

    # Initialize area with all white cells (= 1).
    area = np.ones((width, height), dtype=np.int8)

    for _ in range(num_iter):
        if area[x, y] == 0:
            area[x, y] = 1
            # Turn left
            d -= 1
            if d < 0:
                d = 3
        elif area[x, y] == 1:
            area[x, y] = 0
            # Turn right
            d += 1
            if d > 3:
                d = 0

        # Move ant:
        if d == 0:
            y -= 1
            if y < 0:
                y = height - 1
        elif d == 1:
            x += 1
            if x > width - 1:
                x = 0
        elif d == 2:
            y += 1
            if y > height - 1:
                y = 0
        elif d == 3:
            x -= 1
            if x < 0:
                x = width - 1

    return area


result = ant_model(100, 100, 100000)

# Display the array as an image.
plt.imshow(result, cmap="gray", interpolation="nearest")
plt.colorbar()
plt.show()
