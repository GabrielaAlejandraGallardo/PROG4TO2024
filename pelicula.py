Peliculas_Drama = ['The Hangover', 'Superbad', 'Anchorman', 'Bridesmaids', 'Deadpool']
Peliculas_Comedia =['The Shawshank Redemption', 'Forrest Gump', 'Titanic', 'The Godfather', 'Schindler\'s List']
Peliculas_Suspenso = ['The Exorcist', 'The Shining', 'Psycho', 'Halloween', 'A Nightmare on Elm Street']
Peliculas_Temor = ['Se7en', 'The Silence of the Lambs', 'Gone Girl', 'Shutter Island', 'Prisoners']


Peliculas= (Peliculas_Drama,Peliculas_Comedia,Peliculas_Suspenso,Peliculas_Temor)

def cargarPeliDrama():
      Pelicula_Drama = input ("¿ Que pelicula quiere agregar ? : ")
      Peliculas_Drama.append(Peliculas_Drama)

def cargarPeliComedia():
    Pelicula_Comedia = input ("¿ Que pelicula quiere agregar ? : ")
    Peliculas_Comedia.append(Pelicula_Comedia)
    
def cargarPeliSuspenso():
    Pelicula_Suspenso = input ("¿ Que pelicula quiere agregar ? : ")
    Peliculas_Suspenso.append(Pelicula_Suspenso)   
    
def cargarPeliTerror():
    Pelicula_Temor = input ("¿ Que pelicula quiere agregar ? : ")
    Peliculas_Temor.append(Pelicula_Temor)     

def mostarPelis():    
    for i in Peliculas:
        print(i)
while True:
    Menu_1 = input (" Elija una opcion : \n 1- Cargar Peliculas \n 2- Mostrar peliculas \n 3-Salir \n >>>>")
    if Menu_1 == "1":
        Menu_2 = input ("Cual es el genero de la pelicula que quiere cargar: \n 1-Drama \n 2-Comedia \n 3-Suspenso \n 4-Temor \n >>>>")
        if Menu_2 == "1":
           # Pelicula_Drama = input ("¿ Que pelicula quiere agregar ? : ")
            #Peliculas_Drama.append(Peliculas_Drama)
            cargarPeliDrama()
            print("¡Realizado!")
        elif Menu_2 == "2":
            cargarPeliComedia()
            print("¡Realizado!")
        elif Menu_2 == "3":
            cargarPeliSuspenso()
            print("¡Realizado!")
        elif Menu_2 == "4":
            cargarPeliTerror()
            print("¡Realizado!")
        else:
            print("La opcion que ha seleccionado no se encuentra dentro de las opciones")
    elif Menu_1== "2":
        mostarPelis()
    elif Menu_1== "3":
        print("Saliendo del programa...")
        break
    else:
        print("La opcion que ha seleccionado no se encuentra dentro de las opciones")    
