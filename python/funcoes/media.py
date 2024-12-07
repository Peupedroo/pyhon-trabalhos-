def media (lista):
    soma = 0
    numero = len(lista)
    for i in lista:
         soma+=i
    me = soma / numero
    return me

listo = [1,2,3,4]
l = [1,8,9,7,6,12,3,4,6,23,423,4,12,412,341,234,132,12,4,12,4,123,12,4,1,243,12,4]

oda = media(listo)
da = media (l)

print (da)
print (oda)