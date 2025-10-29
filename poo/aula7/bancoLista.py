from contas import Conta


class BancoLista:

    def __init__(self):
        self.contas = []
        
    def cadastrar(self, conta: Conta):
        # no momento de cadastrar uma conta, também é necessário cadastrar o banco ao qual essa conta pertence
        self.contas.append(conta)
    
    def bloquear_conta(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            conta.bloquear()
            print(f"a conta {numero} foi bloqueada com sucesso!")
        else:
            print("a conta não foi encontrada!")
        
    def desbloquear_conta(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            conta.desbloquear()
            print(f"a conta {numero} foi desbloqueada com sucesso!")
        else:
            print("a conta não foi encontrada!")
    def get_total_contas(self):
        if not self.contas:
            print("não há nenhuma conta cadastrada")
            return 0
        total = len(self.contas)
        print(f"o total de contas atualmente equivale a {total}")
        return total
        
    
    def get_total_bancos(self):
        bancos = {conta.banco for conta in self.contas}
        if not bancos:
            print("não há nenhum banco cadastrado!")
            return 0
        total = len(bancos)
        print(f"o total de bancos atualmente equivale a {total}")
        return total

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
    
    def remover_conta(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            self.contas.remove(conta)
            print(f"a conta {numero} foi removida com sucesso!")

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

    def listar_bancos(self):
        bancos = sorted({conta.banco for conta in self.contas})
        if not bancos:
            print("não há nenhum banco cadastrado!")
        print(bancos)
    
    def listar_contas(self):
        if not self.contas:
            print("eu sinto muito mas atualmente não ha nenhuma conta cadastrada!")
            return 
        for conta in self.contas:
            print(f"conta: {conta.get_numero()} - banco: {conta.get_banco()} - agencia: {conta.get_agencia()}")

# aqui abaixo temos um programa principal para poder testar as classes acima
if __name__ == "__main__": 
    
    
    banco_teste = BancoLista()
    print("Banco teste foi criado.")
    
    # contas testes a partir da classe Conta
    conta_ana = Conta("111-2", "001", "BANCO_A")
    conta_joao = Conta("222-3", "001", "BANCO_A")
    conta_levy = Conta("333-4", "002", "BANCO_B")
    # cadastrando as contas no banco
    banco_teste.cadastrar(conta_ana)
    banco_teste.cadastrar(conta_joao)
    banco_teste.cadastrar(conta_levy)
    print("contas de Ana, João e Levy cadastradas no banco.")
    # testando o método bloquear_conta
    banco_teste.bloquear_conta("111-2")
    # testando o método desbloquear_conta
    banco_teste.desbloquear_conta("111-2")
    
    banco_teste.listar_bancos() 
      
    banco_teste.saldo("111-2")
    banco_teste.creditar("111-2", 43)
    banco_teste.saldo("111-2")