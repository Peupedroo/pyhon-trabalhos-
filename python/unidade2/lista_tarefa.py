lista = []

i = 0

while i < 5:
    perg = input("o que deseja adicionar na lista")
    print ("se deseja parar escreva (!)")

    adicionando = lista.append(perg)
     
    i+=1
print (lista)