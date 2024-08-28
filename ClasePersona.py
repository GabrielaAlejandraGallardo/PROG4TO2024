class Persona:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def mostrar(self):
     print("Edad:",self.age,"\nNombre:",self.name)
     print("_____________________________________")
     
class Profesor(Persona):
  def __init__(self, name, age,antiguedad):
    super().__init__(name, age)
    self.antiguedad=antiguedad
    
  def mostrar(self):
    print("antiguedad:",self.antiguedad)
    return super().mostrar()  
   
pro= Profesor("Paula", 38,18)
pro.mostrar()

p = Persona("Juana", 50)
p.mostrar()

