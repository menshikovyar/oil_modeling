import numpy as np
import matplotlib.pyplot as plt
from solver import solve

N1_0 = 100      # начальная концентрация бензина
N2_0 = 50       # начальная концентрация дизеля
N3_0 = 0        # начальная концентрация мазута
N1_in = 50      # входная концентрация бензина
N2_in = 100     # входная концентрация дизеля
T = 1           # коэффициент превращения бензина в дизель
P = 0.5         # коэффициент превращения дизеля в мазут
k1 = 0.1        # скорость поступления бензина
k3 = 0.05       # скорость поступления дизеля
t_end = 10      # время окончания моделирования

# Решение уравнений без учета зависимости от температуры
t, solution_no_temp = solve(N1_0, N2_0, N3_0, N1_in, N2_in, T, P, k1, 0.05, k3, 0.02, t_end, temperature_dependence=False)

# Решение уравнений с учетом зависимости от температуры
A_with_temp = 1.5
E_a_with_temp = 20
k2_with_temp = 0.05 * A_with_temp * np.exp(-E_a_with_temp / (8.314 * 293))  # Примерные значения для с учетом температурной зависимости
k4_with_temp = 0.02 * A_with_temp * np.exp(-E_a_with_temp / (8.314 * 293))  # Примерные значения для с учетом температурной зависимости
t, solution_with_temp = solve(N1_0, N2_0, N3_0, N1_in, N2_in, T, P, k1, k2_with_temp, k3, k4_with_temp, t_end, temperature_dependence=True)

# Определение максимальных значений концентраций для установки пределов графика
max_concentration = max(np.max(solution_no_temp), np.max(solution_with_temp))

plt.figure(figsize=(10, 8))

# Первый график: изменение концентрации нефтепродуктов во времени
plt.subplot(2, 2, 1)
plt.plot(t, solution_no_temp[:, 0], label='Бензин без темп.')
plt.plot(t, solution_no_temp[:, 1], label='Дизель без темп.')
plt.plot(t, solution_with_temp[:, 0], label='Бензин с темп.')
plt.plot(t, solution_with_temp[:, 1], label='Дизель с темп.')
plt.xlabel('Время, часы')
plt.ylabel('Концентрация, г/л')
plt.title('Изменение концентрации нефтепродуктов во времени')
plt.legend()
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)

# Второй график: изменение скорости реакций во времени
plt.subplot(2, 2, 2)
reaction_rate_benzine_to_diesel = k2_with_temp * solution_with_temp[:, 0] * T * t
reaction_rate_diesel_to_mazut = k4_with_temp * solution_with_temp[:, 1] * P * t
plt.plot(t, reaction_rate_benzine_to_diesel, label='Скорость реакции: бензин -> дизель')
plt.plot(t, reaction_rate_diesel_to_mazut, label='Скорость реакции: дизель -> мазут')
plt.xlabel('Время, часы')
plt.ylabel('Скорость реакции, л/ч')
plt.title('Изменение скорости реакций во времени')
plt.legend()
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.tight_layout()
plt.show()
