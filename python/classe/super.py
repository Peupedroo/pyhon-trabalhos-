class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
class Super_heroi(Pessoa):
    def __init__(self, nome, idade, voar):
        super().__init__(nome, idade,)
        self.voar = voar
    def voando (self):
        print ("voandooo")


person = Pessoa ("pedro", 19)

heroi = Super_heroi("sipider", 20, False)

print (person.idade)
heroi.voando()