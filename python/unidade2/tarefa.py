lista = [1, 3, 4, 5, 6, 7, 8]

i = 0

while i < len(lista):
    print (lista)
    i+=1

    if i == 3:
        del lista[3]

    
print (lista)