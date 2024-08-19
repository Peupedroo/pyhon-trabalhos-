L = [1, 2, 3, 4, 5, 6]


i = 0 
media = 0
for numero in L:
   
    if numero % 2 == 0:
        i += numero


for j in L:
    if j % 2 == 0:
       media += 1

calculo = i / media

print (media)   
print (i)
print (calculo)
