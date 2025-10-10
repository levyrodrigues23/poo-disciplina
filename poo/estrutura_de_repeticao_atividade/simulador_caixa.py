
    

saque = 0

historico = []

def menu():
    saldo = 1000
    while True:
        print("=== MENU DO CAIXA ELETRONICO === \n")
        opcao = int(input("bem vindo ao caixa eletronico! \n  1 - depositar \n  2 - sacar \n  3 - consultar o saldo \n  4 - ver o histórico de transações \n  5 - sair: \n :"))
    
        if opcao == 1:
            valor_deposito = int(input("digite o valor que voce quer depositar: "))
            saldo += valor_deposito
            historico.append(valor_deposito)
            print(f"deposito de {valor_deposito}")
        elif opcao == 2:
            saldo_usuario = int(input("digite o valor de quanto voce quer sacar: "))
            
            if saldo < saldo_usuario:
                 print("infelizmente voce não possui saldo suficiente!")
                   
            else:
                saldo -= saldo_usuario
                print(f"voce sacou {saldo_usuario}")
                    
        elif opcao == 3:
            print(f"o saldo atual que voce possui equivale a {saldo}")
            
        elif opcao == 4:
            
            for transacao in historico:
                print(f"transacoes registradas: {transacao}")
            
        elif opcao == 5:
            print("tudo bem, tenha um ótimo dia")
            break
        else:
            print("voce digitou uma opção invalida! tente novamente.")
            continue
            
             
            
            
       
menu()
        
    
    
    
    