import numpy as np
from oscillation import calculate_oscillation
from graph import graph_oscillation


def main():
    # Definir el tiempo de 0 a 2 segundos
    t = np.linspace(0, 2, 1000)

    # Calcular la oscilación
    y = calculate_oscillation(t)

    # Graficar el resultado
    graph_oscillation(t, y)



if __name__ == '__main__':
    main()

