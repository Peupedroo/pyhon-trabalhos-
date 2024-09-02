def pessoa (nome, idade, profissao):

    return nome, idade, profissao

def pai (funcao, nome, idade, profissao):
    profissional = funcao(nome, idade, profissao)
    return profissional

o = pai(pessoa,"pedro", "19", "programador")

print (o)