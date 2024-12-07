import math 

class Calcular :
    def __init__(self, raio) :
         self.r = raio
    def calculando_area (self):
        area = math.pi * (self.r**2)
        return area

numero = Calcular(6)

area =numero.calculando_area()

print (area)