class Alumno:
    m=1
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.mostrar()

    def mostrar(self):
        self.mayornota()
        print("Su Nombre: ", self.nombre)
        print("Su Nota:", self.nota)
        if self.nota >= 7:
            print("alumno aprobado")
        else:
            print("alumno reprobado")

    def mayornota(self):
        if self.nota > Alumno.m:
            Alumno.m = self.nota
            print("La mayor nota es:", Alumno.m)
        else:
            Alumno.m = self.nota
            print("La menor nota es:", Alumno.m)

a1 = Alumno("Ana Lopez", 8)
a2 = Alumno("Juan Ledesma", 6)
