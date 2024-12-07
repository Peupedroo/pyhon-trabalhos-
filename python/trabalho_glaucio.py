altura_total = 0
generofemtotal = 0
total_pessoas = 2
maior_altura = 0
menor_altura = 0
for i in range (total_pessoas):
    altura = float(input("qual sua altura: "))
    genero = input("qual o seu genero digite F ou M : ")
    altura_total+=altura


    if altura > maior_altura:
        maior_altura = altura
    
    elif altura < menor_altura:
        menor_altura = altura

    if genero == "F":
        generofemtotal += 1


if altura != 0:
    media = altura_total/total_pessoas
    print (media)



print (f"a maior pessoa mede {maior_altura}")
print (f"total de pessoas com genero feminino {generofemtotal}")
print (f"a menor altura e {menor_altura}")