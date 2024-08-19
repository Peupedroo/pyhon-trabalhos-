L = ["pia", "sofa"]

i = 0

pergunta_1 = input ("verifique se o obejeto esta a lista e qual sera o primeiero " )
pergunta_2 = input ("qual a sua segunda verificacao ")

verificacao = False

while i < len(L):
    if L[i] == pergunta_1:
        verificacao = True
        print (f"esse elemento tem na lista {pergunta_1}")
       
    elif L[i] == pergunta_2:
        verificacao = True
        print (f"esse elemento tem na {pergunta_2}")
    
       
        
    i+=1

if not verificacao:
    print(f"Esses objetos não estão na lista: {pergunta_1}, {pergunta_2}")
