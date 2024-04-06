import numpy as np
def model(y, t, k1, k2, k3, k4, N1_in, N2_in, T, P):
    N1, N2 = y

    dN1_dt = k1 * (N1_in - N1) - k2 * N2 * T * t
    dN2_dt = k3 * (N2_in - N2) - k4 * N1 * P * t

    return [dN1_dt, dN2_dt]
