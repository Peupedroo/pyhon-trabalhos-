import random

aleatorio = random.randint(1, 10)
acerto = False
escolha = int(input("escolha um numero"))
while acerto == False:

    if escolha > aleatorio:
        print ("esse numero e maior escolha um menor")
        escolha = int (input("escolha outro numero"))
        
    elif escolha < aleatorio:
        print ("esse numero e menor escolha um maior")
        escolha = int (input("escolha outro numero"))
    else :
        print ("esse numero e igual ao que oo pc escolheu")
        acerto == True
        break