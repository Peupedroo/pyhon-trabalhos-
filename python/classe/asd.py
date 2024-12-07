class Pessoa :
  def __init__(self, nome , idade):
    self.nome = nome
    self.idade = idade
  def falar (self):
    return f"meu nome e {self.nome} e tenho {self.idade} de idade"
  
pessoa = Pessoa("pedro", 19)
j = pessoa.falar()
print (j)