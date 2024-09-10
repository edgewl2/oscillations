import numpy as np
from oscillation import calculate_oscillation
from graph import graph_oscillation


def main():
    # Parámetros
    u = 1  # Ajusta según sea necesario
    times = np.linspace(0, 2, 1000)  # Tiempo de 0 a 2 segundos

    # Definir valores de n
    ns = [4, 15, 30]
    ys = [calculate_oscillation(times, u, n) for n in ns]

    # Graficar el resultado
    graph_oscillation(times, ys, ns)



if __name__ == '__main__':
    main()

