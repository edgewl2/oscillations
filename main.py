from graph import graph_oscillation


def main():
    # Solicitar número de ciclos
    cycles = int(input('Ingrese el número de ciclos a mostrar en el gráfico: '))

    # Solicitar términos N
    terms_input = input('Ingrese los términos N separados por comas (por ejemplo, 4,15,30): ')
    terms = [int(t) for t in terms_input.split(',')]

    # Graficar el resultado
    graph_oscillation(terms, cycles)



if __name__ == '__main__':
    main()

