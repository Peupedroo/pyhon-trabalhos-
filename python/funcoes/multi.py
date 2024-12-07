def mult (*numeros):
    inicio = 1
    for i in numeros:
        inicio*=i
    return inicio

i = mult(2,2)
print (i)
