""" Módulo temperaturas

Este módulo tiene apenas nos funciones, c2f y f2c, para convertir temperaturas
de Celsius a Fahrenheit y viceversa.
"""

def c2f(c):
    return 1.8 * c + 32

def f2c(f):
    return (f-32) / 1.8
