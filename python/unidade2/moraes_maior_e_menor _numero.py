L = [1, 2, 3, 4, 5]

minimo = L[0]
maximo = L[0]
for i in L:
    if i < minimo :
        minimo = i 
    
print (minimo)

for i in L:
    if i > maximo:
        maximo = i 
    
print (maximo)