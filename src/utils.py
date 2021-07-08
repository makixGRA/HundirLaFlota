import numpy as np


class Tablero:
    def __init__(self):
        self.tablero = np.full((10, 10), " ")

    def introducir_barco(self, tamanio, orient, x, y):
        for i in range(0, tamanio):
            if orient == "N":
                self.tablero[x - i, y] = "*"
            if orient == "S":
                self.tablero[x + i, y] = "*"
            if orient == "E":
                self.tablero[x, y + i] = "*"
            if orient == "O":
                self.tablero[x, y - i] = "*"

    def hay_obstaculos(self, tamanio, orient, x, y):
        hay_obstac = False
        for i in range(0, tamanio):
            if orient == "N" and ((x - tamanio + 1) < 0 or self.tablero[x - i, y] in ["*"]):
                hay_obstac = True
            if orient == "S" and ((x + tamanio) > 10 or self.tablero[x + i, y] in ["*"]):
                hay_obstac = True
            if orient == "E" and ((y + tamanio) > 10 or self.tablero[x, y + i] in ["*"]):
                hay_obstac = True
            if orient == "O" and ((y - tamanio + 1) < 0 or self.tablero[x, y - i] in ["*"]):
                hay_obstac = True
        return hay_obstac

    def init_tablero(self):
        cont1, cont2, cont3, cont4 = 0, 0, 0, 0

        while cont1 < 4 or cont2 < 3 or cont3 < 2 or cont4 < 1:
            if cont1 < 4:
                orient = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.hay_obstaculos(1, orient, coordX, coordY):
                    self.introducir_barco(1, orient, coordX, coordY)
                    cont1 += 1
            if cont2 < 3:
                orient = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.hay_obstaculos(2, orient, coordX, coordY):
                    self.introducir_barco(2, orient, coordX, coordY)
                    cont2 += 1
            if cont3 < 2:
                orient = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.hay_obstaculos(3, orient, coordX, coordY):
                    self.introducir_barco(3, orient, coordX, coordY)
                    cont3 += 1
            if cont4 < 1:
                orient = np.random.choice(["N", "S", "E", "O"])
                coordX = np.random.randint(10)
                coordY = np.random.randint(10)
                if not self.hay_obstaculos(4, orient, coordX, coordY):
                    self.introducir_barco(4, orient, coordX, coordY)
                    cont4 += 1
