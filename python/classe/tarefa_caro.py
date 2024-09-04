class Carro :
    def __init__(self, marca, valor, numero, tanque) :
        self.marca = marca
        self.valor = valor
        self.numero = numero
        self.tanque = tanque
    def modelo (self):
        return f"o marca do carro e {self.marca} o valor e {self.valor} o numero de portas q {self.numero} "
    
    def abastecer  (self, litros):
        if self.tanque >= 100:
            print ("o tanque esta cheio")
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100
        return self.tanque
    def dirigir (self, km):
        km_por_litro = 10
        self.tanque -= (km/ km_por_litro)
        return self.tanque

        
        
carro = Carro("honda", 6000, 4, 100)


a = carro.modelo()
tanque = carro.abastecer(20)
rodagem = carro.dirigir(100)
print (tanque)
print (a)       
print(rodagem)

abastecer = carro.abastecer(20)
print (abastecer)
poe = carro.abastecer(30)
print (poe)