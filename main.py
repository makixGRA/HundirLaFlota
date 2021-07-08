import numpy as np

from utils import Tablero

texto = """

,-----. ,--.,------.,--.  ,--.,--.   ,--.,------.,--.  ,--.,--.,------.   ,-----.       ,---.                         
|  |) /_|  ||  .---'|  ,'.|  | \  `.'  / |  .---'|  ,'.|  ||  ||  .-.  \ '  .-.  '     /  O  \                        
|  .-.  \  ||  `--, |  |' '  |  \     /  |  `--, |  |' '  ||  ||  |  \  :|  | |  |    |  .-.  |                       
|  '--' /  ||  `---.|  | `   |   \   /   |  `---.|  | `   ||  ||  '--'  /'  '-'  '    |  | |  |                       
`------'`--'`------'`--'  `--'    `-'    `------'`--'  `--'`--'`-------'  `-----'     `--' `--'                       
,--.  ,--.,--. ,--.,--.  ,--.,------.  ,--.,------.     ,--.     ,---.      ,------.,--.    ,-----.,--------. ,---.   
|  '--'  ||  | |  ||  ,'.|  ||  .-.  \ |  ||  .--. '    |  |    /  O  \     |  .---'|  |   '  .-.  '--.  .--'/  O  \  
|  .--.  ||  | |  ||  |' '  ||  |  \  :|  ||  '--'.'    |  |   |  .-.  |    |  `--, |  |   |  | |  |  |  |  |  .-.  | 
|  |  |  |'  '-'  '|  | `   ||  '--'  /|  ||  |\  \     |  '--.|  | |  |    |  |`   |  '--.'  '-'  '  |  |  |  | |  | 
"""

print(texto)

print("\n")

print("Para terminar el juego introduce una letra como coordenada.")

print("\n")

jug1 = Tablero()
jug1Impactos = Tablero()
jug2 = Tablero()
jug2Impactos = Tablero()

jug1.init_tablero()
jug2.init_tablero()

print("Tablero inicial del jugador 1")
print(jug1.tablero)
print("\nTablero de impactos del jugador 1")
print(jug1Impactos.tablero)

aciertos1 = 0
aciertos2 = 0
turno_jugador = 1
fin = False

try:
    while (aciertos1 < 3 and aciertos2 < 3) and not fin:
        while turno_jugador == 1:
            x = int(input("Introduce coordenada X entre 0 y 9: "))
            y = int(input("Introduce coordenada Y entre 0 y 9: "))

            if x > 9 or y > 9:
                print("\nError: te has salido del tablero. Jugar de nuevo.")
                print("(Para terminar introduce una letra.)")
                break
            elif jug1Impactos.tablero[x, y] == "X" or jug1Impactos.tablero[x, y] == "A":
                print("\nPosicion ya tomada. Meter nuevas coordenadas.\n")
                break
            elif jug2.tablero[x, y] == "*":
                jug1Impactos.tablero[x, y] = "X"
                aciertos1 += 1
                print("\n¡Barco alcanzado!")
                print("Aciertos Jugador 1:", aciertos1, "\n")
                print("Mi Tablero principal\n")
                print(jug1.tablero, "\n")
                print("Mi Tablero de impactos\n")
                print(jug1Impactos.tablero, "\n")

                if aciertos1 == 3:
                    fin = True
                    print("Ganó el jugador 1")
                    break

            elif jug2.tablero[x, y] == " ":
                jug1Impactos.tablero[x, y] = "A"
                turno_jugador = 2
                print("\n¡Agua!")
                print("Aciertos Jugador 1:", aciertos1, "\n")
                print("Mi Tablero principal\n")
                print(jug1.tablero, "\n")
                print("Mi Tablero de impactos\n")
                print(jug1Impactos.tablero, "\n")

        while turno_jugador == 2 and not fin:

            x = np.random.randint(10)
            y = np.random.randint(10)

            if jug2Impactos.tablero[x, y] == "X" or jug2Impactos.tablero[x, y] == "A":
                break

            elif jug1.tablero[x, y] == "*":
                jug1.tablero[x, y] = "X"
                jug2Impactos.tablero[x, y] = "X"
                aciertos2 += 1
                print("\n¡Barco alcanzado!")
                print("Aciertos Jugador 2:", aciertos2, "\n")
                print("Mi Tablero principal\n")
                print(jug1.tablero, "\n")

                if aciertos2 == 3:
                    fin = True
                    print("Ganó el jugador 2")

            elif jug1.tablero[x, y] == " ":
                jug1.tablero[x, y] = "A"
                jug2Impactos.tablero[x, y] = "A"
                turno_jugador = 1
                print("\n¡Agua!")
                print("Aciertos Jugador 2:", aciertos2, "\n")
                print("Mi Tablero principal\n")
                print(jug1.tablero, "\n")


except ValueError:
    print("\nJuego terminado.")

