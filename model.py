import numpy as np

import numpy as np

def model(y, t, k1, k2, k3, k4, N1_in, N2_in, T, P, temperature_dependence):
    N1, N2, N3 = y
    if temperature_dependence:
        A = 1.0  # Пример значения для параметра A
        E_a = 10.0  # Пример значения для параметра E_a
        k2 *= rate_constant(t, A, E_a)
        k4 *= rate_constant(t, A, E_a)
    dN1_dt = k1 * (N1_in - N1) - k2 * N2 * T * t
    dN2_dt = k3 * (N2_in - N2) - k4 * N1 * P * t
    return dN1_dt, dN2_dt, 0




def rate_constant(t, A, E_a, R=8.314):
    T = t + 273.15  # Преобразование температуры в Кельвины
    return A * np.exp(-E_a / (R * T))
