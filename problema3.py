# Función para calcular los factores primos de un número
def find_prime_factors(n):
    factors = []
    # Verificar divisibilidad por 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Verificar divisibilidad por números impares
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # Si n es un número primo mayor que 2
    if n > 2:
        factors.append(n)
    
    return factors

# Función para encontrar el mayor factor primo de un número
def largest_prime_factor(n):
    prime_factors = find_prime_factors(n)
    return max(prime_factors)

# Número dado en el problema
number = 600851475143

# Calcular y mostrar el mayor factor primo
largest_factor = largest_prime_factor(number)
print("El mayor factor primo del número", number, "es:", largest_factor)
