class Pessoa :
    def __init__(self, nome, idade, profissao) :
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

pedro = Pessoa("pedro", 19, "programador")
funcionario = pedro.nome, pedro.idade, pedro.profissao
print (funcionario)