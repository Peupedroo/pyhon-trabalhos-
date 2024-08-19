l = ["sofa", "televisao", "computador", "radio"]

i = 0
item = input("qual o item que vc procura: ")

encontrado = False
while i < len(l):
    if l[i] == item:
        print (f"ma casa tem {item}")
        encontrado == True
    i+=1


if encontrado == False:
    print ("a casa nao tem isso")
