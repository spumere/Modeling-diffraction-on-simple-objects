import numpy as np
import matplotlib.pyplot as plt
from obstacles import *
from image_processing import *

# все, что имеет размерность, записано в си
# число отсчетов в массиве анализируемого кадра
N = 256
# сторона анализируемого квадратного кадра
l = 0.01
# длина волны
wavelength = 650e-9
# расстояние от препятствия до плоскости оценки дифракционной картины
z = 1
# толщина нити
h = 0.0005
# радиус диска и отверстия
R = 0.001
# ширина прямоугольника
a = 0.001
# высота прямоугольника
b = 0.002

wave = plane_wave(N)
threaded_wave = thread(wave, l, h)
propagated_threaded_wave = ASM(threaded_wave, N, l, wavelength, z)

circled_wave = circle(wave, l, R)
propagated_circled_wave = ASM(circled_wave, N, l, wavelength, z)

holled_wave = hole(wave, l, R)
propagated_holled_wave = ASM(holled_wave, N, l, wavelength, z)

rected_wave = rectangle(wave, l, a, b)
propagated_rected_wave = ASM(rected_wave, N, l, wavelength, z)

fig, axes = plt.subplots(4, 3)

axes[0, 0].set_title('Исходная плоская волна', fontsize = "10")
# параметрами vmin и vmax даем функции imshow диапазон для построения изображения, без них vmin = vmax = 1,
# и изображение будет черным
axes[0, 0].imshow(np.abs(wave), cmap='gray', vmin=0, vmax=1)
axes[0, 1].set_title(f'Плоская волна сразу\n после прохождения через нить толщиной {h} м', fontsize = "10")
axes[0, 1].imshow(np.abs(threaded_wave), cmap='gray', vmin=0, vmax=1)
axes[0, 2].set_title(f'Плоская волна через {z} м\n после прохождения через нить', fontsize = "10")
axes[0, 2].imshow(np.abs(propagated_threaded_wave), cmap='gray')

axes[1, 0].set_title('Исходная плоская волна', fontsize = "10")
axes[1, 0].imshow(np.abs(wave), cmap='gray', vmin=0, vmax=1)
axes[1, 1].set_title(f'Плоская волна сразу после\n прохождения через непрозрачный диск, R = {R} м', fontsize = "10")
axes[1, 1].imshow(np.abs(circled_wave), cmap='gray', vmin=0, vmax=1)
axes[1, 2].set_title(f'Плоская волна через {z} м\n после прохождения непрозрачный диск', fontsize = "10")
axes[1, 2].imshow(np.abs(propagated_circled_wave), cmap='gray')

axes[2, 0].set_title('Исходная плоская волна', fontsize = "10")
axes[2, 0].imshow(np.abs(wave), cmap='gray', vmin=0, vmax=1)
axes[2, 1].set_title(f'Плоская волна сразу после\n прохождения через отверстие, R = {R} м ', fontsize = "10")
axes[2, 1].imshow(np.abs(holled_wave), cmap='gray', vmin=0, vmax=1)
axes[2, 2].set_title(f'Плоская волна через {z} м\n после прохождения через отверстие', fontsize = "10")
axes[2, 2].imshow(np.abs(propagated_holled_wave), cmap='gray')

axes[3, 0].set_title('Исходная плоская волна', fontsize = "10")
axes[3, 0].imshow(np.abs(wave), cmap='gray', vmin=0, vmax=1)
axes[3, 1].set_title(f'Плоская волна сразу после прохождения через непрозрачный\n прямоугольник, a = {a} м, b = {b} м', fontsize = "10")
axes[3, 1].imshow(np.abs(rected_wave), cmap='gray', vmin=0, vmax=1)
axes[3, 2].set_title(f'Плоская волна через {z} м\n после прохождения через непрозрачный прямоугольник', fontsize = "10")
axes[3, 2].imshow(np.abs(propagated_rected_wave), cmap='gray')

plt.show()

    
    