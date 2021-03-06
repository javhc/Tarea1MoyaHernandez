from metodos import check_char
from metodos import caps_switch
from string import ascii_letters

largo = len(ascii_letters)


def test():  # 'check_char' para todo el intervalo
    i = 0
    while i < largo:
        assert check_char(ascii_letters[i]) == 0
        i = i + 1


def test2():  # 'check_char' para todo el intervalo
    e = 0
    while e < largo:
        assert caps_switch(ascii_letters[e]) == ascii_letters[e].swapcase()
        e = e + 1


def test3():  # verifica el punto b del método check_char
    assert check_char('abc') == 0


def test4():  # verifica el punto c del método check_char
    assert check_char('9') == 0


def test5():  # verifica el punto d del método check_char
    assert check_char(10) == 0
