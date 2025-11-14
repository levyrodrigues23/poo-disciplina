from contas import Conta

# seguindo a logica de que eu poderia criar uma matriz, os bancos seriam as linhas e as contas seriam o conteudo das linhas
class BancoLista:

    def __init__(self):
        self.bancos_e_contas = {}
        
    def cadastrar_conta(self, conta: Conta):
        # 1. Pegar o banco da conta e padronizar
        nome_banco = conta.get_banco()  # método que retorna o banco
        nome_banco = nome_banco.upper()  # converter para maiúsculo
    
        # 2. Verificar se o banco existe
        if nome_banco in self.bancos_e_contas:  # operador "está em"
            # 3. Adicionar a conta na lista do banco
            self.bancos_e_contas[nome_banco].append(conta)  # método para adicionar em lista
            print(f"Conta {conta.get_numero()} cadastrada no {nome_banco}.")
        else:
            # 4. Avisar que o banco não existe
            print(f"Erro: O banco '{nome_banco}' não está cadastrado.")
            print("Cadastre o banco primeiro usando cadastrar_banco().")
    
    def cadastrar_banco(self, nome_banco: str):
        # Opcional: padronizar para maiúsculo
        nome_banco = nome_banco.upper()
        
        # Verificar se já existe
        if nome_banco in self.bancos_e_contas:
            print(f"O banco '{nome_banco}' já está cadastrado.")
        else:
            # Criar uma nova "linha" com lista vazia
            self.bancos_e_contas[nome_banco] = []
            print(f"Banco '{nome_banco}' cadastrado com sucesso!")
    
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
        if not self.bancos_e_contas:
            print("não há nenhuma conta cadastrada")
            return 0
        total_contas = len(self.bancos_e_contas.values())
        print(f"o total de contas atualmente equivale a {total_contas}")
        return total_contas
        
    def get_total_bancos(self):
        if not self.bancos_e_contas:
            print("não ha nenhum banco cadastrado")
            return 0
        total_bancos = len(self.bancos_e_contas.keys())
        return print(total_bancos)
    
    def get_banco(self):
        if not self.bancos_e_contas:
            print("não tem nada a ser mostrado atualmente")
            return 0
        for i, banco in enumerate(self.bancos_e_contas):
            print(f"{i}.banco: {banco}")
        return banco
    
    def buscar_conta_pelo_banco(self, banco):
        
    
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



conta = Conta("numero", "agencia", "SANTANDER")

banco = BancoLista()
banco.cadastrar_banco("santander")
banco.cadastrar_banco("pitela")
banco.cadastrar_conta(conta)
banco.get_total_bancos()
banco.get_banco()

