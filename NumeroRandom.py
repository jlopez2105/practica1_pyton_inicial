import random

def adivinar_numero_limitado():
    """
    Este juego le pide al usuario adivinar un número secreto
    generado aleatoriamente entre 1 y 50, con un límite de 5 intentos.
    """
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 50.")
    print("¡Solo tienes 5 intentos para adivinarlo!")

    numero_secreto = random.randint(1, 50)
    intentos = 0
    max_intentos = 5
    adivinado = False

    while not adivinado and intentos < max_intentos:
        try:
            # Muestra cuántos intentos le quedan al usuario
            intentos_restantes = max_intentos - intentos
            intento_usuario = int(input(f"Intento {intentos + 1}/{max_intentos}. ¿Cuál es tu número? "))
            intentos += 1

            if intento_usuario < numero_secreto:
                print("Demasiado bajo. ¡Intenta de nuevo!")
            elif intento_usuario > numero_secreto:
                print("Demasiado alto. ¡Intenta de nuevo!")
            else:
                adivinado = True
                print(f"¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos} intentos!")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    # Si el bucle termina y el número no fue adivinado, es porque se acabaron los intentos
    if not adivinado:
        print("\n¡Oh no! Se te acabaron los intentos.")
        print(f"El número secreto era: {numero_secreto}")
        print("¡Más suerte la próxima vez!")

# Inicia el juego
if __name__ == "__main__":
    adivinar_numero_limitado()
