class Persona









:
    def __init__(self,nom):
        self.nombre=nom

class Padre(Persona):
     def __init__(self, nom, edad):
        super.__init__(nom)
        self.edad=edad

class Hijo(Padre):
    def __init__(self, nom, edad, ps):
        super.__init__(nom,edad)
        self.ps=ps
