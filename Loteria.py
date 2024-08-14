import random

# Diccionario para almacenar los jugadores y sus números
jugadores = {}
historial_sorteos = []

# Función para generar números de lotería
def generar_numero():
    return random.randint(1, 99)  

# Función para comprar un boleto
def comprar_boleto(nombre, cantidad, numeros_elegidos=None):
    if numeros_elegidos:
        numeros = numeros_elegidos
    else:
        numeros = [generar_numero() for _ in range(cantidad)]
    
    if nombre in jugadores:
        jugadores[nombre].extend(numeros)
    else:
        jugadores[nombre] = numeros
    return numeros

# Función para realizar el sorteo
def realizar_sorteo():
    numero_ganador = generar_numero()
    historial_sorteos.append(numero_ganador)
    return numero_ganador

# Función para mostrar el historial de sorteos
def mostrar_historial():
    print("\nHistorial de sorteos:")
    for i, numero in enumerate(historial_sorteos, 1):
        print(f"Sorteo {i}: {numero}")

# Función principal
def main():
    premio_total = 1000.0  # Premio inicial en float
    numero_ganador = 0  # Inicialización del número ganador en int
    rondas_sin_ganador = 0
    limite_rondas = 3  # Límite de rondas sin ganador
    
    while True:
        print("\n1. Comprar boleto")
        print("2. Realizar sorteo")
        print("3. Ver historial de sorteos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese su nombre: ")
            cantidad = int(input("¿Cuántos números desea comprar? "))
            eleccion = input("¿Desea elegir sus propios números? (s/n): ")
            
            if eleccion.lower() == 's':
                numeros_elegidos = []
                for i in range(cantidad):
                    num = int(input(f"Ingrese el número {i+1} (1-999): "))
                    while num < 1 or num > 999:
                        num = int(input("Número inválido. Ingrese un número entre 1 y 999: "))
                    numeros_elegidos.append(num)
                numeros_comprados = comprar_boleto(nombre, cantidad, numeros_elegidos)
            else:
                numeros_comprados = comprar_boleto(nombre, cantidad)
            
            print(f"Ha comprado los siguientes números: {numeros_comprados}")
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
                    rondas_sin_ganador = 0
                    jugadores.clear()
                    premio_total = 1000.0
                else:
                    print("No hay ganadores en esta ronda.")
                    rondas_sin_ganador += 1
                    if rondas_sin_ganador >= limite_rondas:
                        print(f"Se ha alcanzado el límite de {limite_rondas} rondas sin ganador.")
                        print("Se reinicia el juego con nuevos números.")
                        jugadores.clear()
                        premio_total = 1000.0
                        rondas_sin_ganador = 0
                    else:
                        print(f"Los números se mantienen para la siguiente ronda. Rondas sin ganador: {rondas_sin_ganador}")
                
        elif opcion == '3':
            mostrar_historial()
                
        elif opcion == '4':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()