numeros = map(int, input("digite uma lista de números separados por espaço").split())

# Exercicio 2

newList = list(filter(lambda number: number > 0, numeros))
print(newList)

# uso do try except

def input_seguro(prompt):
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("sinto muito, mas a sua entrada nãõ foi validada, ", inputString)
        return input_seguro(prompt)
    
    
    if __name__ == "__main__":
        idade = input_seguro("Por favor, digite sua idade: ")
        print(f"Sua idade é {idade}")   
        