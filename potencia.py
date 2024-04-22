def potencia(a: int, b:int):
    if b == 0: # Todo número elevado a 0 da 1
        return 1
    else:
        return a * potencia(a, b-1) # a**b = a * a**(b-1)
    
