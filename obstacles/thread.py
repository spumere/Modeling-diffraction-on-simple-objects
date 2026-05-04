import numpy as np

def thread(wave, l, h):
    wave_copy = wave.copy() 
    N = len(wave_copy)
    x = np.linspace(-l/2, l/2, N)
    y = np.linspace(-l/2, l/2, N)
    X,Y = np.meshgrid(x,y)
    thread = (X < h/2) & (X > -h/2) 
    return np.where(thread, wave_copy, 0) 