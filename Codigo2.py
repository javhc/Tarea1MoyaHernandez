import re #Se importa una libreria, la cual no se va a utilizar

#Se define una funcion que recibe un nombre y devuelve True si se encuentra dentro de una lista de nombres
def isondatabase(nombre):
    listaNombres = ["Aharon", "Juan", "Pedro", "José"]
    var1 = 1 #Se crea una variable que no se usa
    for i in listaNombres:
        if nombre == i:
            return True
        if var2 == 2: #La variable var2 no existe
            return True
    return False
