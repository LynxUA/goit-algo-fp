import matplotlib.pyplot as plt
import numpy as np

def draw_pythagorean_tree(ax, x, y, angle, size, level):
    if level == 0:
        return

    x2 = x + size * np.cos(angle)
    y2 = y + size * np.sin(angle)

    x3 = x2 - size * np.sin(angle)
    y3 = y2 + size * np.cos(angle)

    x4 = x - size * np.sin(angle)
    y4 = y + size * np.cos(angle)

    ax.plot([x, x2, x3, x4, x], [y, y2, y3, y4, y], 'k-')

    new_size = size * np.sqrt(2) / 2

    draw_pythagorean_tree(ax, x4, y4, angle + np.pi / 4, new_size, level - 1)

    draw_pythagorean_tree(ax, x3, y3, angle - np.pi / 4, new_size, level - 1)

def create_pythagorean_tree(level):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    size = 1
    angle = 0
    x, y = 0, 0

    draw_pythagorean_tree(ax, x, y, angle, size, level)

    plt.show()

level = int(input("Введіть рівень рекурсії (наприклад 5): "))
create_pythagorean_tree(level)
