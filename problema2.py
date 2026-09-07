# Problema de Project Euler: Suma de términos pares en la secuencia Fibonacci que no exceden 4 millones

def suma_pares_fibonacci(maximo):
    a, b = 1, 2
    total = 0
    
    while a <= maximo:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    
    return total

# Calcular la suma de términos pares en la secuencia Fibonacci que no exceden 4 millones
resultado = suma_pares_fibonacci(4_000_000)

# Mostrar el resultado por consola
print("La suma de los términos pares en la secuencia Fibonacci que no exceden 4 millones es:", resultado)
