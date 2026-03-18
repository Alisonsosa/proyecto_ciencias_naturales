def calcular_posicion(x0, v, t):
    """x = x0 + v * t"""
    return x0 + v * t

def calcular_velocidad(x, x0, t):
    """v = (x - x0) / t"""
    return (x - x0) / t

def calcular_tiempo(x, x0, v):
    """t = (x - x0) / v"""
    if v == 0:
        raise ValueError("La velocidad no puede ser cero para calcular el tiempo.")
    return (x - x0) / v

def menu_mru():
    print("\n--- Calculadora MRU ---")
    print("1. Calcular posición (x = x0 + v·t)")
    print("2. Calcular velocidad (v = (x - x0)/t)")
    print("3. Calcular tiempo (t = (x - x0)/v)")
    print("0. Salir")

while True:
    menu_mru()
    opcion = input("Elige opción: ")

    try:
        if opcion == "1":
            x0 = float(input("Posición inicial (x0): "))
            v = float(input("Velocidad constante (v): "))
            t = float(input("Tiempo (t): "))
            x = calcular_posicion(x0, v, t)
            print(f"Posición final = {x}")

        elif opcion == "2":
            x = float(input("Posición final (x): "))
            x0 = float(input("Posición inicial (x0): "))
            t = float(input("Tiempo (t): "))
            v = calcular_velocidad(x, x0, t)
            print(f"Velocidad constante = {v}")

        elif opcion == "3":
            x = float(input("Posición final (x): "))
            x0 = float(input("Posición inicial (x0): "))
            v = float(input("Velocidad constante (v): "))
            t = calcular_tiempo(x, x0, v)
            print(f"Tiempo = {t}")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError as e:
        print("Error:", e)