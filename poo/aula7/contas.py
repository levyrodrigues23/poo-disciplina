
class Conta:
    
    def __init__(self, numero, agencia, banco):
        self.numero = numero
        self.saldo = 0.0
        self.agencia = agencia
        self.bloqueado = False
        self.banco = banco
        
    def creditar(self, valor):
        if self.bloqueado:
            print("a conta está bloqueada, não é possível realizar o deposito!")
            return
        self.saldo += valor

    def debitar(self, valor):
        if self.bloqueado:
            print("a conta está bloqueada, não é possível realizar o saque!")
            return
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("voce está com saldo insuficiente!")
    def get_saldo(self):
        return self.saldo
    
    def get_numero(self):
        return self.numero
    
    def get_agencia(self):
        return self.agencia
    
    def get_banco(self):
        return self.banco
    
    def bloquear(self):
        self.bloqueado = True
        print(f"a conta {self.numero} foi bloqueada com sucesso")
    
    def desbloquear(self):
        self.bloqueado = False
        print(f"a conta {self.numero} foi desbloqueada com sucesso")
    
    def encerrar_conta(self):
        self.saldo = 0.0
        print(f"a conta {self.numero} foi encerrada com sucesso!")
        
    def alterar_banco(self, novo_banco):
        self.banco = novo_banco
        print(f"o banco da conta {self.numero} foi alterado para {novo_banco} com sucesso!")
        
    def alterar_agencia(self, nova_agencia):
        self.agencia = nova_agencia
        print(f"a agencia da conta {self.numero} foi alterada para {nova_agencia} com sucesso!")
        


