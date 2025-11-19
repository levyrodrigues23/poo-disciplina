valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
soma = 0


for i in range(valor1, valor2 + 1):
    impar = i % 2 != 0
    if impar:
        print(i)
        soma += i
    
print(soma)
        
        
        
    
    
