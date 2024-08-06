import random

# Diccionario para almacenar los jugadores y sus numeros
jugadores = {}

# Función para generar números de loteria
def generar_numero():
    return random.randint(1, 99)

# Funcion para comprar un boleto
def comprar_boleto(nombre, cantidad):
    numeros = [generar_numero() for _ in range(cantidad)]
    if nombre in jugadores:
        jugadores[nombre].extend(numeros)
    else:
        jugadores[nombre] = numeros
    return numeros

# Función para realizar el sorteo
def realizar_sorteo():
    return generar_numero()

# Funcion principal
def main():
    premio_total = 1000.0  # Premio inicial en float
    numero_ganador = 0  # Inicialización del número ganador en int
    
    while True:
        print("\n1. Comprar boleto")
        print("2. Realizar sorteo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese su nombre: ")
            cantidad = int(input("¿Cuántos números desea comprar? "))
            numeros_comprados = comprar_boleto(nombre, cantidad)
            print(f"Ha comprado los siguientes números: {numeros_comprados}")
            
            # Uso de operador de asignación
            premio_total += cantidad * 10
            
        elif opcion == '2':
            if not jugadores:
                print("No hay jugadores. No se puede realizar el sorteo.")
            else:
                numero_ganador = realizar_sorteo()
                print(f"El número ganador es: {numero_ganador}")
                
                ganadores = []
                for nombre, numeros in jugadores.items():
                    if numero_ganador in numeros:
                        ganadores.append(nombre)
                
                if ganadores:
                    premio_individual = premio_total / len(ganadores)
                    print("¡Tenemos ganadores!")
                    for ganador in ganadores:
                        print(f"{ganador} ha ganado ${premio_individual:.2f}")
                else:
                    print("No hay ganadores en esta ronda.")
                
                # Reiniciar el juego
                jugadores.clear()
                premio_total = 1000.0
                
        elif opcion == '3':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()