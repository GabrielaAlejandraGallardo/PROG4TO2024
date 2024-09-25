Actividad 1: 
Crear una clase Vehiculo que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más 
las cuales son Moto y Carro.
Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
Agregar una funcion que determine un descuento del 10% en el precio de llanta mayor a 100.000 pesos




Actividad 2:
Crear un programa que contenga los datos personales de personas que forman parte de una escuela: estudiantes y docentes.
Deberas identificar los siguientes atributos y aplicarlos a Clases en POO: matricula, dni, nombreApellido, direccion, anioCurso, materias, cursosAcargo.
crear funciones para mostrar sus datos.
Crear 3 objetos para cada clase


evaluación

https://colab.research.google.com/drive/1H9qiHtXhrd8LIYYOm2JvYfP7qqW-S_YW?usp=sharing



Autoevaluación  POO HERENCIA Y POLIMORFISMO : https://forms.gle/ZJ7g81Ku79xKfW5h8  https://colab.research.google.com/notebooks/intro.ipynb
class Animal:
  def __init__(self,nombre, edad, raza, historial,datosDuenios):
    self.nombre=nombre
    self.edad=edad
    self.raza=raza
    self.historial=historial
    self.datosDuenios=datosDuenios
    
  def mostrar(self):
    print(f"NOMBRE {self.nombre}, edad:{self.edad}, raza: {self.raza}, historial: {self.historial}, datosDuenios: {self. datosDuenios}")  
  
class Gato(Animal):  
  def __init__(self,nombre, edad, raza, historial,datosDuenios,orejas,cola, unias):
     super().__init__(nombre, edad, raza, historial,datosDuenios)
     self.orejas=orejas
     self.cola=cola
     self.unias=unias
  def mostrar(self):   
    super().mostrar()
    print(f" Orejas: {self.orejas} COLA:{self.cola}, Unias:{self.unias}")

class Consulta:
  def __init__(self, fecha,tipo, precio):
    # Added indented block with a pass statement 
    pass # This is a null operation; nothing happens when it executes.


a1=Animal("pepe",2,"belga","garrapatas","juam telefon: 304945855")
a1.mostrar()
g1=Gato("pepito",2,"siames","garrapatas y pulgas","juana telefon: 304945345", 2, 1, "filosas" )
g1.mostrar()


Evaluación POO HERENCIA Y POLIMORFISMO:https://forms.gle/KhoM45FPnuMQUk6N9
