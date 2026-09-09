def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


contador = 0
numero = 1

while contador < 10001:
    numero += 1

    if es_primo(numero):
        contador += 1

print("El primo número 10.001 es:", numero)
