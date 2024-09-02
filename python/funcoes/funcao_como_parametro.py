def soma (a, b):
    return a + b
def mult (a, b):
    return a * b

def operacao (a, b, f):
    resultado = f(a, b)
    return resultado


o = operacao (5, 5, soma)
i = operacao (5, 5, mult)

print (o)
print (i)