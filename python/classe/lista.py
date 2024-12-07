import random


maior = 0

L = []
def lista():
    global maior
    for i in range(10):
        L.append(random.randint(0, 10))
    
    for i in L:    
        if i > maior:
            maior = i

        
    print (maior)
    return L
   


    

o = lista()

print (o)
