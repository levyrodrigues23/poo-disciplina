def apresentar_paragrafo(nome, idade, altura, peso, nacionalidade):
    return print(f"Oi, meu nome é {nome} e tenho {idade} anos. Atualmente, meu peso equivale a {peso} kg e minha altura é de {altura} m. A minha nacionalidade é {nacionalidade}.")



while True:

    nome = input("Digite seu nome: ")
    nacionalidade = input("Digite sua nacionalidade: ")
    
    if nome.isalpha() == False and nacionalidade.isalpha() == False:
        print("voce deve digitar apenas letras")
        continue
    
    try:
        idade = int(input("Digite sua idade: "))
        altura = float(input("digite a sua altura: "))
        peso = float(input("digite o seu peso: "))
        
    except ValueError:
        print("voce deve digitar apenas números")
        continue
    
    apresentar_paragrafo(nome, idade, altura, peso, nacionalidade)
    break
        
    

  
   
    




            
            
         
            
            
       