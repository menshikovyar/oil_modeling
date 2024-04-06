import numpy as np
from scipy.integrate import odeint

def model(y, t, k1, k2, k3, k4, N1_in, N2_in, T, P):
    N1, N2, N3 = y
    dN1_dt = k1 * (N1_in - N1) - k2 * N2 * T * t
    dN2_dt = k3 * (N2_in - N2) - k4 * N1 * P * t
    dN3_dt = k2 * N2 * T * t + k4 * N1 * P * t
    return [dN1_dt, dN2_dt, dN3_dt]

def solve(N1_0, N2_0, N3_0, N1_in, N2_in, T, P, k1, k2, k3, k4, t_end):
    t = np.linspace(0, t_end, 1000)  # Генерируем временные шаги
    y0 = [N1_0, N2_0, N3_0]  # начальные условия
    solution = odeint(model, y0, t, args=(k1, k2, k3, k4, N1_in, N2_in, T, P))
    return t, solution
