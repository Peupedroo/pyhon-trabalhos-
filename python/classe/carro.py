class Carro :
    def __init__(self, portas, motor , teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca 
        self.preco = preco
    
modelo = Carro(4, 2.0, "tem", "bmw", 18000)

print (type (modelo))
print (modelo.marca)
print(modelo.motor)
print(modelo.portas)
print(modelo.preco)
print(modelo.teto_solar)