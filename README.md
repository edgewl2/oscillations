# Visualización de Oscilaciones Sinusoidales.

## Series de Fourier (Suma de Ondas Periódicas)
Actualmente este proyecto genera visualizaciones de series de Fourier para diferentes números de términos (N), 
con enfoque a aquellas que usan **coseno** o conocidas como **onda periódica** o **aproximada a onda cuadrada**.

![demo](https://github.com/user-attachments/assets/ba0c824d-8778-4dff-abe5-7c6395376a75)

### Requisitos:
- Python 3.7+
- NumPy
- Matplotlib

### Instalación:
1. Clona este repositorio o descarga los archivos.
2. (Opcional pero recomendado) Crea un ambiente virtual:
```sh
python -m venv venv
```
   
   Activa el ambiente virtual:
   - En Windows:
```sh
venv\Scripts\activate
```
   - En macOS y Linux:
```sh
source venv/bin/activate
```

3. Instala las dependencias necesarias:
```sh
pip install -r requirements.txt 
```

### Uso:
Ejecuta el script principal:
```sh
python main.py
```

Esto solicitará el número de ciclos, además de los terminos que usará para generar gráfica para series de Fourier con 
distintos términos.

Estructura del Proyecto:
- constants.py: Contiene constantes utilizadas en todo el proyecto.
- oscillation.py: Define las funciones para calcular los coeficientes y la oscilación.
- graph.py: Contiene la función para graficar las series de Fourier.
- main.py: Script principal para ejecutar el programa.

**NOTA:**
Este proyecto muestra cómo la aproximación de la serie de Fourier mejora a medida que se aumenta el número de términos (N). Observa cómo la forma de la onda se vuelve más definida con valores más altos de N.