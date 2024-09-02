a = 10
b = 8
c = 12

def maior (numero):
  resultado = ""

  if numero > 10 :
    resultado = "e maior que 10"
    
  elif numero < 10:
    resultado = "menor que 10"
    
  else:
    resultado = "e 10"
    
  return resultado

i = maior (c)
j = maior (b)
o = maior (a)
l = maior (b)


print (i)
print (j)
print (o)        
print (l)