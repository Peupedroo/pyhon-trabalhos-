class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome 
        self.idade = idade
        self.profissao = profissao
    def __str__(self):
        return f"o nome do usuario {self.nome}, idade {self.idade}, profisao {self.profissao}"

pedro = Pessoa("pedro", 19, "programador")

print   (pedro.__str__())
