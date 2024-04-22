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

   