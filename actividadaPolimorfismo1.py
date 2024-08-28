#Crear una clase Vehiculo que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más 
# las cuales son Moto y Carro.
#Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
#Agregar una funcion que determine un descuento del 10% en el precio de llanta mayor a 100.000 pesos
class Vehiculo:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    def mostrar(self):
        print("La cantidad de llantas: ",self._llantas,"El color es:",self._color,"El precio es:",self._precio)
    
    def precioConDescuento(self):
        if self._precio > 100000:
            print("Precio con descuento:", self._precio * 0.9)
        else:
            print("El producto no tiene descuento")

class Moto(Vehiculo):
    def __init__(self, llantas, color, precio, manubrio):
        super().__init__(llantas, color, precio)
        self.manubrio=manubrio
        
    def mostrar(self):
        super().mostrar()    
        print("Manubrio",self.manubrio)
    

class Carro(Vehiculo):
    def __init__(self, llantas, color, precio, volante):
        super().__init__(llantas, color, precio)
        self.volante=volante
        
    def mostrar(self):
        super().mostrar()   
        print("Volante: ",self.volante)

print("OBJETO = moto1")
moto1 = Moto(2, "Gris", 200000, "corto")
moto1.mostrar()
moto1.precioConDescuento()

print("OBJETO = carro1")
carro1 = Carro(4, "Negro", 60000,"plastico")
carro1.mostrar()
carro1.precioConDescuento()

