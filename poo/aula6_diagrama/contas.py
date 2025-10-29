from bancoLista import BancoLista


class Conta:
    
    def __init__(self, numero, agencia):
        self.numero = numero
        self.saldo = 0.0
        self.agencia = agencia

    def creditar(self, valor):
        self.saldo += valor


    def debitar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("voce está com saldo insuficiente!")

    def get_saldo(self):
        return self.saldo



# aqui abaixo temos um programa principal para poder testar as classes acima
if __name__ == "__main__": 
    
    
    banco_teste = BancoLista()
    print("Banco teste foi criado.")


    # criando algumas contas, ou falando melhor, instanciando objetos do tipo Conta
    conta_ana = Conta("111-2", "001") # o primeiro valor corresponde ao numero da conta e o outro a agencia
    conta_joao = Conta("222-3", "001")
    conta_levy = Conta("333-4", "002")
    print("\n respectivas contas criadas para ana, joao e levy.")

    # ao passo que as contas foram criadas, chega o passo de cadastrá-las no banco
    banco_teste.cadastrar(conta_ana)
    # o mesmo poderia ter sido feito como banco_teste.cadastrar(Conta("111-2", "001")), funcionaria da mesma forma, mas preferi deixar mais performático.
    banco_teste.cadastrar(conta_joao)
    banco_teste.cadastrar(conta_levy)
    print("\n contas de Ana, João e Levy cadastradas no banco.")

    # testando a parte de creditar, ou seja, depositar
    print("\n--- testando depositos ---")
    banco_teste.creditar("111-2", 1500.50)
    banco_teste.creditar("222-3", 800.00)
    
    # testando consulta de saldo
    print("\n--- consultando saldo ---")
    banco_teste.saldo("111-2")
    banco_teste.saldo("222-3")
    # testando saques (debitar)
    print("\n--- testando saques ---")
    print("sacando r$ 300.00 da conta da ana.")
    banco_teste.debitar("111-2", 300.00)
    banco_teste.saldo("111-2")

    print("\ntentando sacar r$ 1000.00 da conta do joão (saldo insuficiente).")
    banco_teste.debitar("222-3", 1000.00)
    banco_teste.saldo("222-3")

    # testando transferência
    print("\n--- testando transferência ---")
    print("transferindo r$ 500.00 da ana para o joão.")
    banco_teste.transferir("111-2", "222-3", 500.00)

    # verificando os saldos finais
    print("\n--- consultando saldos finais ---")
    banco_teste.saldo("111-2")
    banco_teste.saldo("222-3")

    # testando com uma conta que não existe
    print("\n--- testando operação em conta inexistente ---")
    banco_teste.saldo("999-9")