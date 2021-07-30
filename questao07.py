
def verificar(str, max, min):
    valor = len(str)
    if valor <= max and min <= valor:
        return True
    return False


print(verificar("jennifer", 8, 1))
