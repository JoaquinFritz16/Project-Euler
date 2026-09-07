# Problema 1 de Project Euler: Suma de múltiplos de 3 o 5 menores que 1000

def suma_multiplos():
    total = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Mostrar el resultado por consola
print("La suma de los múltiplos de 3 o 5 menores que 1000 es:", suma_multiplos())
