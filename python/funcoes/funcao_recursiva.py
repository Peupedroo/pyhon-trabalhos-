def soma_ate_100 (n):
    if n < 100:
        n+= 1
        print (n)
        return soma_ate_100(n)
        
    else :
        return "pronto"

numero = 94

n = soma_ate_100(numero)

print (n)
         