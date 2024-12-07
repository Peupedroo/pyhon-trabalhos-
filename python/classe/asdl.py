import random 
L = []
def lista ():
  for i in range (0, 10):
    L.append(random.randint(0, 10))
  return L
def verificacao():
  pares = []
  for i in L:
    if i % 2 == 0:
      pares.append(i)
  return f"esses numerosao pares {pares}"

j = lista()
i = verificacao ()


print (j)
print (i)