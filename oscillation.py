import numpy as np
from constants import Ao, omega


def calculate_oscillation(t):
    """
    Calcula el desplazamiento en función del tiempo para un oscilador armónico simple.

    :param t: El tiempo (puede ser un array o un valor escalar)
    :return: El desplazamiento en el tiempo t
    """
    return Ao * np.sin(omega * t)
