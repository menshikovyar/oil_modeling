import numpy as np
import matplotlib.pyplot as plt


def plot_results(t, N1, N2, N3):
    t_shifted = t - t[0]  # Смещаем ось времени к нулю

    plt.figure(figsize=(10, 6))
    plt.plot(t_shifted, N1, label='Бензин')
    plt.plot(t_shifted, N2, label='Дизель')
    plt.plot(t_shifted, N3, label='Мазут')
    plt.xlabel('Время')
    plt.ylabel('Концентрация')
    plt.title('Динамика концентрации нефтепродуктов')
    plt.legend()
    plt.grid(True)
    plt.axis([0, max(t_shifted), 0, 150])  # Установка начала координат в точку (0,0) и пределов осей
    plt.show()
