import matplotlib.pyplot as plt
import numpy as np

# Define la función cuadrática
def funcion_cuadratica(x, a, b, c):
  return a * x**2 + b * x + c

# Define los coeficientes
a = 2
b = -3
c = 1

# Crea un rango de valores de x
x = np.linspace(-5, 5, 100)

# Calcula los valores de y correspondientes
y = funcion_cuadratica(x, a, b, c)

# Crea la gráfica
plt.plot(x, y)

# Agrega etiquetas a los ejes
plt.xlabel("x")
plt.ylabel("y")

# Agrega un título a la gráfica
plt.title("Gráfica de una función cuadrática")

# Muestra la gráfica
plt.show()