import matplotlib.pyplot as plt

def plot_results(t, N1, N2, N3):
    plt.plot(t, N1, label='Бензин')
    plt.plot(t, N2, label='Дизель')
    plt.plot(t, N3, label='Мазут')
    plt.xlabel('Время')
    plt.ylabel('Концентрация')
    plt.title('Изменение концентрации нефтепродуктов во времени')
    plt.legend()
    plt.grid(True)
    plt.show()
