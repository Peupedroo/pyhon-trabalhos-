class Banco:
    def __init__(self, nome, saldo, cpf):
        self.saldo = saldo
        self.nome = nome 
        self.cpf = cpf
    def depositar (self, deposito):
        saldo_total = self.saldo + deposito
        return saldo_total
    def transferencia (self, pix):
        if pix > self.saldo :
            print ("vc nao tem saldo suficiente ")
        else :
            saldo_total =  self.saldo - pix
            return saldo_total
    def saque (self, sacanagem):
        if sacanagem > self.saldo:
            print ("vc nao tem dinheiro")
        else :
            saldo_total =  self.saldo - sacanagem
            return saldo_total
    

conta = Banco("pedro", 1500, 2800)

deposito = conta.depositar (1500)

trasferencia = conta.transferencia (600)
saque = conta.saque(900)
ss = conta.saque(900)
ssa = conta.saque (900)

print (conta)
print (deposito)
print (trasferencia)
print (saque)
print (ss)
print (ssa)