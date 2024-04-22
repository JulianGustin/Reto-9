#Calcular MCD con algoritmo de Euclides
def mcd(a: int, b: int):
    # Si b es cero, el MCD es a
    if b == 0:
        return a
    # Llama a b y el residuo de a%b
    else:
        return mcd(b, a % b)

if __name__ == "__main__":
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el segundo numero: "))

    # Llama a la funcion
    resultado = mcd(n1, n2)

    # Imprime el resultado
    print(f"El Maximo comun divisor de {n1} y {n2} es: {resultado}")
