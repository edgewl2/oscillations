import matplotlib.pyplot as plt


def graph_oscillation(t, ys, ns):
    """
    Genera la gráfica de la oscilación en función del tiempo.

    :param t: Array de tiempos
    :param y: Array de desplazamientos
    :param n: Número máximo de términos en la serie
    """
    n_plots = len(ns)
    fig, axes = plt.subplots(n_plots, 1, figsize=(10, 8), sharex=True)

    for i in range(n_plots):
        axes[i].plot(t, ys[i])
        axes[i].set_title(f"Oscilación con {ns[i]} términos")
        axes[i].set_ylabel("Desplazamiento")
        axes[i].grid(True)

    axes[-1].set_xlabel("Tiempo (s)")
    plt.tight_layout()
    plt.show()