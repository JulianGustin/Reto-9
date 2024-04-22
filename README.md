# Reto 9
### Julian Jacobo Gustin Moreno
![logo](https://camo.githubusercontent.com/a12903c4e2f58575622e5cc1222df41a66748bec5311fb8b769d680428dbb9ff/68747470733a2f2f692e6962622e636f2f767652785072622f412d616469722d756e2d742d74756c6f2e706e67)
***

### Ejercicio 1: Cree una función que permita calcular el Máximo Comun Divisor de dos números dados (a y b).
```python
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

```
***
### Ejercicio 2: Cree una función anónima que calcule:
```python
if __name__ == "__main__":
    x = float(input("Ingrese el valor de 'x': "))
    if x == 1:  # El denominador no puede ser 0
        print("Valor invalido")
    else: 
        funcion = (lambda x: x/(x**(1/3)-1))(x) # Funcion anonima
        print (f"f({x}) es igual a {funcion}")
```

***
### Ejercicio 3: Cree una función que reciba dos números y un parametro con el cual se decida si regresa el mayor o el menor, por defecto debe regresar el mayor.

```python
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
```

***
## 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
#### Funcion 1 : Reto 6 (Carne)
#### Original
```python
def peso_aves(n:float, m:float, k:float ) -> float: 
    pesoN = n*6
    pesoM = m*7 
    pesoK = k*1
    pesoTotal = pesoN + pesoM + pesoK 
    return pesoTotal 
```
#### Lambdas 
```python
if __name__ == "__main__":
    n = float(input("Ingrese el número de gallinas: "))  # Entrada del número de gallinas
    m = float(input("Ingrese el número de gallos: "))  # Entrada del número de gallos
    k = float(input("Ingrese el número de pollitos: "))  # Entrada del número de pollitos

    cantidadCarne = (lambda n, m, k: n * 6 + m * 7 + k * 1 )(n, m, k)  # Funcion de calculo peso total lambda 
    print("La cantidad de carne en kilos es:", cantidadCarne)  # Salida del resultado
```
#### Funcion 2 : Reto 6 (Compra)
#### Original
```python
def precio_compra(p:float, m:float, h:float ) -> float: 
    precioP = p*300
    precioM = m*3300 
    precioH = h*350
    precioTotal = precioP + precioM + precioH
    return precioTotal 
```
#### Lambdas 
```python
if __name__ == "__main__": 
    p = float(input("Ingrese el numero de panes a comprar: "))
    m = float(input("Ingrese el numero de bolsas de leche a comprar: "))
    h = float(input("Ingrese el numero de huevos a comprar: "))
    B = float(input("Ingrese cuánta plata le da su mamá: "))

    precio = (lambda p, m, h: p * 300 + m * 3300 + h * 350)(p,m,h)

    resultado = B - precio
    if resultado < 0:
        print("Quedó debiendo ", (resultado*-1), "pesos")
    elif resultado > 0:
        print("Le sobraron ", resultado, "pesos")
    else:
        print("Issss, exactico.")
```
#### Funcion 3 : Reto 6 (Prestamo)
#### Original
```python
def valor_prestamo(C:float, i:float, n:float) ->float: 
    valor = C * (1 + i)**n
    return valor
```
#### Lambdas 
```python
if __name__ == "__main__":
    C = float(input("Ingrese el monto del prestamo: "))
    i = float(input("Ingrese la tasa de interes mensual (decimal) "))
    n = int(input("Ingrese el numero de meses: "))

    valor_final = (lambda C, i, n: C * (1 + i)**n)(C, i, n)

    print("El valor de su prestamo después de ", n, "meses será de ", valor_final)
```
***
## 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
#### Funcion 1 : Reto 6 (Promedio)
#### Original
```python
def promedio(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    promedio = (n1+n2+n3+n4+n5)/5
    return promedio
```
#### Args 
```python
def promedio(*args) ->float:
    suma = 0
    c = 0
    for n in args: 
        suma += n
        c += 1
    promedio = suma/c
    return promedio

prom = promedio(1,2,3,4,5)
print(prom)
    
```
#### Funcion 2 : Reto 6 (Promedio Multiplicativo)
#### Original
```python
def promedio_multiplicativo(n1, n2, n3, n4, n5) ->float:
    multi : float = n1, n2, n3, n4, n5
    promedioMulti = multi**(1/5)
    return promedioMulti

```
#### Args
```python
def promedio_multiplicativo(*args) ->float:
    producto = 1
    c = 0
    for n in args:
        producto *= n
        c += 1
    promedio_multiplicativo = producto ** (1/c)
    return promedio_multiplicativo

prom_multi = promedio_multiplicativo(1, 2, 3)  
print(prom_multi) 
```
#### Funcion 3 : Reto 6 (ordenar)
#### Original
```python
def ordernar(n1:float, n2:float, n3:float, n4:float, n5:float) ->float:
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3
    if n4 > n5:
        n4, n5 = n5, n4
    
    return n1, n2, n3, n4, n5
```
#### Args 
```python
def ordenar(*args):
    numeros = list(args)
    return numeros.sort
```
## 3. Escriba una función recursiva para calcular la operación de la potencia.
```python
def potencia(a: int, b:int):
    if b == 0: # Todo número elevado a 0 da 1
        return 1
    else:
        return a * potencia(a, b-1) # a**b = a * a**(b-1)
```
***
## 4. Pruebas de Fibonacci con time
```python
import time 

def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo
def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)
  

if __name__ == "__main__": 
  n = int(input("Ingrese un número: ")) #Ingresar el número para hacer las pruebas
  start_time = time.time() #Empezar temporizador
  fibon = fibo(n) #Realizar funcion
  end_time = time.time() #Terminar temporizador
  timer1 = end_time - start_time #Encontrar tiempo

#Se repiten los mismos pasos
  start_time = time.time()
  fibor = fiboRecursivo(n)
  end_time = time.time()
  timer2 = end_time - start_time

#Encontrar la diferencia para que sea positiva
  if timer1 > timer2:
    dif = timer1 -timer2
  else:
    dif = timer2 - timer1

  print(f"La funcion 'fibo' con iteración es de {str(timer1)} segundos, la funcion 'fibo' recursiva es de {str(timer2)} segundos y la diferencia entre las dos es de {dif}")
```
Cuando n es 35, la diferencia de tiempo es casi de 1, por lo que diría que es significativa
***
## StackOverflow
![Imagen](https://i.ibb.co/6msmVMH/Captura-de-pantalla-2024-04-22-164831.png)
***
## Linkedin
Link: https://www.linkedin.com/in/juliangustin/
