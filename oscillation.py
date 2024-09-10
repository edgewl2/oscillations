import numpy as np

from constants import PI


def Ao():
    """
    Altura media de la onda
    :return: float
    """
    return (2 * PI**2) / 3

def An(n):
    """
    Coeficiente An de la expansión de Fourier
    :param n int: El número del armónico (debe ser >= 1).
    :return float
    """
    return (1 / (n**2)) * (-1)**n

def generate_oscillation(x, N):
    """
    Genera una oscilación como una suma de cosenos basada en la serie de Fourier.
    :param x float: Posición angular
    :param N int: Número de términos(armónicos) en la serie
    :return float : Valor de la la función periódica aproximada en el punto x
    """
    return Ao() / 2 + sum(An(n) * np.cos(n * x) for n in range(1, N+1))
