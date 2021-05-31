"""Programa principal."""


def verificar_si_es_numero_primo(numero):
    """
    Esta función comprueba si el número es primo.

    Verifica si un número entero entre 0 y 100 es un número primo,
    devolviendo "ES PRIMO" en caso afirmativo o "NO ES PRIMO" en
    caso negativo; si el número está fuera del rango de 0 a 100,
    la función devuelve "ERROR".

    Parameters
    ----------
    numero (int) : Cualquier valor entero.

    Returns
    -------
    resultado (string) : Texto que indica cualquiera de los resultados
                         posibles: es número primo, no lo es, o es error.
    """
    # Declaramos la variable "resultado" y asumimos
    # desde el principio que vamos a obtener un error.
    resultado = "ERROR"

    # Verificamos que la condición del ejemplo se cumpla,
    # que sea un valor entre 0 y 100 inclusive. En caso de
    # no cumplirse, la variable resultado ya tiene lo que
    # se debe devolver.
    if 0 <= numero <= 100:

        # Asumimos que el número no es primo.
        resultado = "NO ES PRIMO"

        # Verificamos que el número sea mayor que 1, ya que
        # el 0 y el 1 no son números primos por definición.
        # En caso de no cumplirse la condición, la variable
        # resultado ya tiene lo que se debe devolver.
        if numero > 1:

            # Asumimos que el número puede ser primo.
            puede_ser_primo = True

            # El primer divisor posible es 2.
            divisor = 2

            # El ciclo continúa mientras pueda ser primo
            # y el divisor sea menor que el número que se
            # está verificando. Usamos un ciclo pre-prueba
            # ya que uan vez que confirmamos que es divisible
            # por un divisor, no es necesario checar los
            # divisores restantes.
            while puede_ser_primo and divisor < numero:

                # Si el módulo es distinto de cero, todavía
                # es posible que sea primo.
                puede_ser_primo = numero % divisor != 0
                divisor += 1

            # Si al final pudo ser primo, entonces es primo.
            if puede_ser_primo:
                resultado = "ES PRIMO"

    # Resultado de la función
    return resultado


# Comienza el código principal.
for numero_por_validar in range(-10, 111):
    print(numero_por_validar, " : ",
          verificar_si_es_numero_primo(numero_por_validar))
