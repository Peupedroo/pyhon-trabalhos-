

def par (l):
    nova_lista = []
    for i in l:
        if i %2 == 0:
           nova_lista.append(i)
    return f"esses numeros sao pares{nova_lista}"

L = [1, 2, 3 , 4 , 5, 8, 12, 15, 18]

lista = par (L)

print (lista)

kiks = [1213, 312, 4, 82394, 340434,4324455667543,23446773451432,5434513245,6,252,45234,543,512,43,2345,3463,45,13521,45,2351435,345345,346356456,456467]

al = par(kiks)

print (al)