import numpy as np
from scipy.integrate import odeint
from model import model

def solve(N1_0, N2_0, N3_0, N1_in, N2_in, T, P, k1, k2, k3, k4, t_end, temperature_dependence=False):
    t = np.linspace(0, t_end, 1000)
    N0 = [N1_0, N2_0, N3_0]
    solution = odeint(model, N0, t, args=(k1, k2, k3, k4, N1_in, N2_in, T, P, temperature_dependence))
    return t, solution
