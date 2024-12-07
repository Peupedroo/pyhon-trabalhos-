l = [1, 2 ,3 ,4 ,5 ]

numero = int(input("digite: "))

encontrado = False
for i in l:
    if i == numero:
    
        print (i)
        encontrado = True

if encontrado == False:
    print ("esse ngc nem existe")