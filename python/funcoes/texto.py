T = "pedro manoel silva gouveia"


def texto (dado):
    reposta = ""

    if len(dado) > 20:
        resposta = "esse dado e grande"
    else :
        resposta = "eesse e pequeno"
    return resposta
        


pergunta = str (input("digite um nome "))

print (texto(T))

inf = texto(pergunta)

print (inf)