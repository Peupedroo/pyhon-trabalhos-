def saudacao (nome):
    return f"ola {nome}"

sds = saudacao("matheus")

print (sds)

def funcao (x):
    return (x + 1)

s = funcao(+1)

print (s)

def profissao (nome):
    p = ""
    
    if nome == "pedro":
        p = "programador"
    else :
        p = "medico"
    
    return p
name = profissao(str(input("qual e o seu nome ")))

print (name)
