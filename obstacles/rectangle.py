import numpy as np

def rectangle(wave, l, a, b):
    wave_copy = wave.copy() 
    N = len(wave_copy)
    x = np.linspace(-l/2, l/2, N)
    y = np.linspace(-l/2, l/2, N)
    X, Y = np.meshgrid(x, y)
    rectangle = ((Y < b/2) & (Y > -b/2)) & ((X < a/2) & (X > -a/2))
    return np.where(rectangle, wave_copy, 0) 