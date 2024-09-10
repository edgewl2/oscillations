import numpy as np
from constants import Ao, omega


def calculate_oscillation(t, u, n):
    """
    Calcula el desplazamiento en función del tiempo para una oscilación basada en una serie de Fourier truncada.

    :param t: El tiempo (puede ser un array o un valor escalar)
    :param u: Amplitud de los armónicos
    :param n: Número máximo de términos en la serie de Fourier
    :return: El desplazamiento en el tiempo t
    """
    omega = 2 * np.pi  # Frecuencia angular (1 Hz)
    y = Ao  # Componente constante

    for k in range(1, n + 1):
        An = (u / k**2) * (-1)**k
        y += An * np.sin(k * omega * t)

    return y
