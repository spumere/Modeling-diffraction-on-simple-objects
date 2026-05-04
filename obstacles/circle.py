import numpy as np

def circle(wave, l, R):
    wave_copy = wave.copy() 
    N = len(wave_copy)
    x = np.linspace(-l/2, l/2, N)
    y = np.linspace(-l/2, l/2, N)
    X,Y = np.meshgrid(x,y)
    circle = X**2 + Y**2 > R**2
    return np.where(circle, wave_copy, 0) 
