def funcion_cuadratica(x, a, b, c):
   return a * x**2 + b * x + c
"""Calcula el valor de una función cuadrática.

  Args:
    x: El valor de entrada.
    a: El coeficiente del término cuadrático.
    b: El coeficiente del término lineal.
    c: El término constante.

  Returns:
    El valor de la función cuadrática.
  """
# Define los coeficientes
a = 2
b = -3
c = 1

# Calcula el valor de la función para x = 5
x = 5
y = funcion_cuadratica(x, a, b, c)

# Imprime el resultado
print(f"El valor de la función cuadrática para x = {x} es {y}")    