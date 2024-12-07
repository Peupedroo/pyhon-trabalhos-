def sequencia (*argumentos):
    for i in argumentos:
        print (i)



def soma (*numeros ):
    sum = 0 
    for num in numeros:
        sum += num
    return sum

r = soma (4,6)

print (r)