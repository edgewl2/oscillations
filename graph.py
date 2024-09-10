import matplotlib.pyplot as plt


def graph_oscillation(t, y):
    """
    Genera la gráfica de la oscilación en función del tiempo.

    :param t: Array de tiempos
    :param y: Array de desplazamientos
    """
    plt.figure(figsize=(8, 6))
    plt.plot(t, y)
    plt.title("Oscilación Armónica Simple")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Desplazamiento")
    plt.grid(True)
    plt.show()
