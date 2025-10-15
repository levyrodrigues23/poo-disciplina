estoque_comida = {"sanduiche": 2, "estrogonofe": 4, "macarrão": 7, "goiaba": 9, "carne": 4, "frango": 5, "pastel": 3, "miojo": 7, "bolinha": 8, "sardinha": 4}
estoque_bebida = {"água": 20, "café": 15, "chá": 10, "suco": 12, "refrigerante": 18, "cerveja": 25, "vinho": 8, "cachaça": 5, "energético": 7, "leite": 14}

def mostrar_estoque():
    print("-- estoque de comida --")
    if not estoque_comida:
        print("não há nenhuma comida no estoque")
    else:
        for comida, quantidade in estoque_comida.items():
            print(f"{comida} possui uma quantidade de {quantidade}")
    print("-- estoque de bebida --")
    if not estoque_bebida:
        print("não há nenhuma bebida no estoque")
    else:
        for bebida, quantidade in estoque_bebida.items():
            print(f"{bebida} possui uma quantidade de {quantidade}")

def adicionar_produto(nome, quantidade):
    global estoque_comida, estoque_bebida
    tipo = input("digite se o produto é comida (a) ou bebida (b): ").lower()
    if tipo == "a":
        estoque = estoque_comida
    elif tipo == "b":
        estoque = estoque_bebida
    else:
        print("tipo inválido")
        return
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"{nome} adicionado com sucesso")

def remover_produto(nome, quantidade):
    global estoque_comida, estoque_bebida
    tipo = input("é comida (a) ou bebida (b)? ").lower()
    if tipo == "a":
        estoque = estoque_comida
    elif tipo == "b":
        estoque = estoque_bebida
    else:
        print("tipo inválido")
        return
    if nome in estoque:
        if estoque[nome] >= quantidade:
            estoque[nome] -= quantidade
            print(f"{quantidade} de {nome} removido.")
            if estoque[nome] == 0:
                print(f"{nome} esgotado do estoque.")
        else:
            print("quantidade insuficiente no estoque.")
    else:
        print("produto não encontrado")

def consultar_produto(nome):
    if nome in estoque_comida:
        print(f"a comida {nome} possui uma quantidade de {estoque_comida[nome]}")
    elif nome in estoque_bebida:
        print(f"a bebida {nome} possui uma quantidade de {estoque_bebida[nome]}")
    else:
        print("produto não encontrado em nenhum estoque.")

def salvar_relatorio():
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("-- estoque de comida --\n")
        for comida, quantidade in estoque_comida.items():
            arquivo.write(f"{comida}: {quantidade}\n")
        arquivo.write("-- estoque de bebida --\n")
        for bebida, quantidade in estoque_bebida.items():
            arquivo.write(f"{bebida}: {quantidade}\n")
    print("relatório salvo como estoque.txt.")

def repor_automatico():
    min_estoque = 5
    for comida in estoque_comida:
        if estoque_comida[comida] < min_estoque:
            print(f"repondo {comida}: {estoque_comida[comida]} -> {min_estoque}")
            estoque_comida[comida] = min_estoque
    for bebida in estoque_bebida:
        if estoque_bebida[bebida] < min_estoque:
            print(f"repondo {bebida}: {estoque_bebida[bebida]} -> {min_estoque}")
            estoque_bebida[bebida] = min_estoque
    print("reposição automática concluída.")

def menu():
    while True:
        print("\n---------- sistema de controle de estoque modular com funções ----------")
        print("a. mostrar estoque")
        print("b. adicionar produto")
        print("c. remover produto")
        print("d. consultar produto")
        print("e. salvar relatório")
        print("f. repor automático")
        print("g. sair")
        opcao = input("digite uma das opções: ").lower()
        if opcao == "a":
            mostrar_estoque()
        elif opcao == "b":
            nome = input("digite o nome do produto: ").lower()
            quantidade = input("digite a quantidade do produto: ")
            if quantidade.isdigit():
                adicionar_produto(nome, int(quantidade))
            else:
                print("quantidade inválida")
        elif opcao == "c":
            nome = input("digite o nome do produto a ser removido: ").lower()
            quantidade = input("digite a quantidade a ser removida: ")
            if quantidade.isdigit():
                remover_produto(nome, int(quantidade))
            else:
                print("quantidade inválida")
        elif opcao == "d":
            nome = input("digite o nome do produto para consultar: ").lower()
            consultar_produto(nome)
        elif opcao == "e":
            salvar_relatorio()
        elif opcao == "f":
            repor_automatico()
        elif opcao == "g":
            print("tudo bem, tenha um ótimo dia")
            break
        else:
            print("opção inválida! tente novamente!")

menu()
