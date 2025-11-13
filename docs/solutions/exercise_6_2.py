import numpy as np
import matplotlib.pyplot as plt
import random


# Helper function to check if position is in bounds.
def in_area(x, y, width, height):
    return (x >= 0) and (x < width) and (y >= 0) and (y < height)


# Helper function to check if given position is full.
# Will be called recursively on all 4 neighbours.
def check_position(area, x, y, width, height):
    if area[x, y] >= 4:
        area[x, y] = 0
        x1 = x - 1
        x2 = x + 1
        y1 = y - 1
        y2 = y + 1

        if in_area(x1, y1, width, height):
            area[x1, y1] += 1
            check_position(area, x1, y1, width, height)
        if in_area(x1, y2, width, height):
            area[x1, y2] += 1
            check_position(area, x1, y2, width, height)
        if in_area(x2, y1, width, height):
            area[x2, y1] += 1
            check_position(area, x2, y1, width, height)
        if in_area(x2, y2, width, height):
            area[x2, y2] += 1
            check_position(area, x2, y2, width, height)


# Create the area and iterate.
def sandpile_model(width, height, num_iter):
    if width < 5:
        raise ValueError(f"Width must be at least 5: {width}")

    if height < 5:
        raise ValueError(f"Height must be at least 5: {height}")

    area = np.zeros((width, height), dtype=np.int8)

    for _ in range(num_iter):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        area[x, y] += 1
        check_position(area, x, y, width, height)

    return area


result = sandpile_model(10, 10, 500)

# Display the array as an image.
plt.imshow(result, cmap="winter", interpolation="nearest")
plt.colorbar()
plt.show()
