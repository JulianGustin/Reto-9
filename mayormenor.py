def mayor_menor(a:int, b:int, c:str="mayor"): # Por defecto, c devuelve mayor
    if c == "menor":  # Si c es menor
        if a < b: # Determina el menor
            return a
        else:
            return b
    else:
        if a > b:  # Determina el mayor
            return a
        else:
            return b
            
   

if __name__ == "__main__":
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    if a == b:
        print("Los valores son iguales")
    else: 
        c = str(input("Desea saber el mayor o el menor?: "))
        respuesta = mayor_menor(a,b,c)
        print(f"Entre {a} y {b} el {c} es {respuesta}")