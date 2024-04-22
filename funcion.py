if __name__ == "__main__":
    x = float(input("Ingrese el valor de 'x': "))
    if x == 1:  # El denominador no puede ser 0
        print("Valor invalido")
    else: 
        funcion = (lambda x: x/(x**(1/3)-1))(x) # Funcion anonima
        print (f"f({x}) es igual a {funcion}")