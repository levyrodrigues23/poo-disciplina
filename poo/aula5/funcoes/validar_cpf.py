def calcular_primeiro_digito(cpf):
    valor = 10
    soma = 0
    
    for i in range(9):
        
        soma += int(cpf[i]) * valor
        valor -= 1
        
    resto = soma % 11
    if resto < 2:
        return '0'
            
    else:
        return str(11 - resto)

    
def calcular_segundo_digito(cpf):
    valor = 11
    soma = 0
    
    for i in range(10):
        soma += int(cpf[i]) * valor
        valor -= 1
    
       
    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)


def validar_cpf():
    
    while True:
        usuario_cpf = input("digite o seu cpf: ")
        
        if not usuario_cpf.isdigit():
            print("voce deve digitar apenas numeros!")
            continue
        if len(usuario_cpf) > 11:
            print("voce digitou valores demais!")
            continue
        elif len(usuario_cpf) < 11:
            print("voce não digitou valores suficientes!")
            continue
         
        primeiro_digito = calcular_primeiro_digito(usuario_cpf)
        segundo_digito = calcular_segundo_digito(usuario_cpf)
        
        if usuario_cpf[-2:] == primeiro_digito + segundo_digito:
            print("o seu cpf é valido")
        else:
            print("o seu cpf é inválido")

        break    
        
        

validar_cpf()
