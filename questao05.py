def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None


lista = [11, 20, 10, 6]
print(pesquise(lista, 10))
