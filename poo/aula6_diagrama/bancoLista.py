class BancoLista:

    def __init__(self):
        self.contas = []
        
    def cadastrar(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def creditar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta não encontrada!")

    def debitar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
                conta.debitar(valor)
        else:
            print("Conta não encontrada!")

    def saldo(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            print(f"Saldo da conta {numero}: {conta.get_saldo()}")
            return conta.get_saldo()
        else:
            print("a conta não foi encontrada")
            return None

    def transferir(self, origem, destino, valor):
        conta_origem = self.buscar_conta(origem)
        conta_destino = self.buscar_conta(destino)
        if conta_origem and conta_destino:
            if conta_origem.saldo >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
            else:
                print("Saldo insuficiente na conta de origem!")
        else:
            print("Conta de origem ou destino não encontrada!")
