
numero = int (input("digite um numero "))
contador = numero
conta = 0
while contador > 0:
    
    if numero % contador == 0:
        conta += 1
    
    contador -=1
    

if conta == 2:
    print ("esse numero e primo")
elif conta> 2:
    print ("esse numero nao e primo")