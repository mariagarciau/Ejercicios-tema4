"""Escriba el mismo algoritmo, pero utilizando dos variables buleanas para comprobar el estado del agua,
sin comparaciones en los SI.
"""
si = True
no = False
def es_gaseoso(temperatura):
    if temperatura>100:
        return si
    else:
        return no
def es_liquido(temperatura):
    if temperatura>=0 and temperatura<=100:
        return si
    else:
        return no
def es_solido(temperatura):
    if temperatura<0:
        return si
    else:
        return no