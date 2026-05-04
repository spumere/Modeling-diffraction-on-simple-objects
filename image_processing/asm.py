import numpy as np

def ASM(wave, N, l, wavelength, z, inverse=False):
    # метод углового спектра по Goodman J. Introduction to Fourier Optics [In Russian]. Moscow: Mir; 1970
    dx = l/N
    nu_x = np.fft.fftfreq(N, dx)
    nu_y = np.fft.fftfreq(N, dx)
    Nu_x, Nu_y = np.meshgrid(nu_x, nu_y, indexing='ij')
    
    sqrt_argument = wavelength**(-2) - Nu_x**2 - Nu_y**2
    
    H = np.zeros_like(sqrt_argument, dtype=complex)
    
    # распространяющиеся волны
    propagating_mask = sqrt_argument >= 0
    H[propagating_mask] = np.exp(-1j * 2 * np.pi * z * np.sqrt(sqrt_argument[propagating_mask]))
    
    # эванесцентные волны 
    evanescent_mask = sqrt_argument < 0
    H[evanescent_mask] = 0
    
    if inverse:
        # для обратного распространения
        H[propagating_mask] = np.exp(1j * 2 * np.pi * z * np.sqrt(sqrt_argument[propagating_mask]))
        # для обратных эванесцентных волн
        H[evanescent_mask] = 0

    return np.fft.ifft2(np.fft.fft2(wave) * H)