import math

# --- Biblioteca MRUA ---
def velocidad_final_vf_v0_a_t(v0, a, t):
    """Vf = v0 + a*t"""
    return v0 + a * t

def aceleracion_a_vf_v0_t(vf, v0, t):
    """a = (Vf - v0) / t"""
    return (vf - v0) / t

def posicion_x_promedio_vf_v0_t(vf, v0, t):
    """x = ((Vf + v0)/2) * t"""
    return ((vf + v0) / 2) * t

def posicion_x_v0_a_t(v0, a, t):
    """x = v0*t + 1/2*a*t^2"""
    return v0 * t + 0.5 * a * t**2

def velocidad_final_cuadrado_vf2_v0_a_x(v0, a, x, x0=0):
    """Vf = sqrt(v0^2 + 2*a*(x - x0))"""
    return math.sqrt(v0**2 + 2 * a * (x - x0))

# --- Menú para usar la biblioteca ---
def menu():
    print("\n--- Calculadora MRUA ---")
    print("1. Calcular velocidad final (Vf = v0 + a·t)")
    print("2. Calcular aceleración (a = (Vf - v0) / t)")
    print("3. Calcular posición usando velocidad promedio (x = ((Vf + v0)/2) · t)")
    print("4. Calcular posición (x = v0·t + 1/2·a·t²)")
    print("5. Calcular velocidad final con posiciones (Vf = sqrt(v0² + 2·a·(x - x0)))")
    print("0. Salir")

while True:
    menu()
    opcion = input("Elige opción: ")

    if opcion == "1":
        v0 = float(input("Velocidad inicial (v0): "))
        a = float(input("Aceleración (a): "))
        t = float(input("Tiempo (t): "))
        vf = velocidad_final_vf_v0_a_t(v0, a, t)
        print(f"Velocidad final = {vf}")

    elif opcion == "2":
        vf = float(input("Velocidad final (Vf): "))
        v0 = float(input("Velocidad inicial (v0): "))
        t = float(input("Tiempo (t): "))
        a = aceleracion_a_vf_v0_t(vf, v0, t)
        print(f"Aceleración = {a}")

    elif opcion == "3":
        vf = float(input("Velocidad final (Vf): "))
        v0 = float(input("Velocidad inicial (v0): "))
        t = float(input("Tiempo (t): "))
        x = posicion_x_promedio_vf_v0_t(vf, v0, t)
        print(f"Posición = {x}")

    elif opcion == "4":
        v0 = float(input("Velocidad inicial (v0): "))
        a = float(input("Aceleración (a): "))
        t = float(input("Tiempo (t): "))
        x = posicion_x_v0_a_t(v0, a, t)
        print(f"Posición = {x}")

    elif opcion == "5":
        v0 = float(input("Velocidad inicial (v0): "))
        a = float(input("Aceleración (a): "))
        x = float(input("Posición final (x): "))
        x0 = float(input("Posición inicial (x0): "))
        vf = velocidad_final_cuadrado_vf2_v0_a_x(v0, a, x, x0)
        print(f"Velocidad final = {vf}")

    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
        la ley de la conservacion de la masa
        ecuacion lineal 
        tiene que ser una ecuacion donde haya una cantidad de atomos por´porcionados 