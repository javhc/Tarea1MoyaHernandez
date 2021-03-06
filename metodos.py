def check_char(entrada):

    import re

    if type(entrada) == str:  # prueba que la entrada sea un string
        lista = len(entrada)  # calcula la cantidad de elementos en el string
        valid = re.fullmatch("[A-Za-z]", entrada)  # str tenga un alfanumérico
    else:
        lista = 0
        valid = 0

    if valid:
        result = 0  # result con str es carac alfanumérico
    else:
        result = 2  # código error: str es carac no alfanumérico

    if lista >= 2:
        result = 1  # código error: str trae más de un caracter

    if type(entrada) != str:
        result = 3  # código de error cuando dato no es un str

    return result


def caps_switch(parametro):

    resultado = check_char(parametro)  # asigna return check_char a 'resultado'

    if resultado == 0:  # pregunta si check_char devolvió un valor correcto
        parametro2 = parametro.swapcase()  # cambio may a min o viceversa
        return parametro2  # devuelve el caracter invertido

    else:
        return resultado  # devuelve código error de función check_char
