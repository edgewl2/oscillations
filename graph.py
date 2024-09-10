import matplotlib.pyplot as plt
import numpy as np

from constants import PI, X_MIN, NUM_POINTS
from oscillation import generate_oscillation


def graph_oscillation(values, cycles):
    """
    Grafica las oscilaciones basadas en la serie de Fourier para diferentes valores de N
    :param values list: Una lista de enteros donde cada entero representa el número de términos (N)
    :param cycles int: Número de ciclos a mostrar en el gráfico
    """
    x_max = cycles * (2 * PI)  # Ajusta X_MAX para cubrir más ciclos
    x = np.linspace(X_MIN, x_max, NUM_POINTS)

    fig, axs = plt.subplots(len(values), 1, figsize=(12, 4 * len(values)))
    fig.suptitle('Series de Fourier para diferentes números de términos (N)')

    for i, N in enumerate(values):
        y = generate_oscillation(x, N)
        axs[i].plot(x, y)
        axs[i].set_title(f'N = {N} términos')
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('f(x)')
        axs[i].grid(True)
        axs[i].set_xlim(X_MIN, x_max)

    plt.tight_layout()
    plt.show()