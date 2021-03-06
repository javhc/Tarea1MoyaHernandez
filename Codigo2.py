# Se define una funcion que recibe un nombre y devuelve True si se encuentra dentro de una lista de nombres
def isondatabase(nombre):
    listaNombres = ["Aharon", "Juan", "Pedro", "José"]
    for i in listaNombres:
        if nombre == i:
            return True
    return False
