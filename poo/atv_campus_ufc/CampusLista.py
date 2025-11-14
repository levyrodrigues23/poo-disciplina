class UfcCampus:
    def __init__(self):
        self.campus = {} # pensando em usar dicionario para q eu possa armazenar diretamente os cursos em listas
        
    def cadastrar_campus(self, nome_campus: str):
        
        nome_campus = nome_campus.lower()
        if nome_campus in self.campus:
            print(f"o campus '{nome_campus}' ja esta cadastrado\n")
        self.campus[nome_campus] = []
        print(f"o respectivo {nome_campus} foi adicionado \n")
        return print(self.campus)
    
    def cadastrar_curso_campus(self, nome_campus: str, curso_novo: str):
        nome_campus = nome_campus.lower()
        if not nome_campus.lower() in self.campus:
            print("esse campus não foi cadastrado aqui ainda.")
        
        self.campus[nome_campus].append(curso_novo)
        print(self.campus)
        
        # é bem provavel que eu mude essa logica futuramente aplicando outro arquivo so para os comandos relacionados aos cursos.
        
    def verificar_os_campus(self):
        if not self.campus:
            print("nenhum campus foi cadastrado aqui ainda.")
            return
        print(f"Aqui estão os respectivos campus e seus cursos\n")
        for i, (chave, valor) in enumerate(self.campus.items()):
            print(f"{i}: Campus: {chave}, Cursos: {valor}. Quantidade de Cursos: {len(self.campus[chave])}")
        
    def remover_campus(self, nome_campus: str):
        nome_campus = nome_campus.lower()
        
        if nome_campus not in self.campus:
            print("esse campus não foi cadastrado aqui ainda.")
            return
        
        cursos_removidos = self.campus.pop(nome_campus)
        print(f"o campus {nome_campus} foi removido.")
        print(f"Cursos que estavam nele: {cursos_removidos}")
        print(self.campus)
        
    def remover_curso_campus(self, nome_curso: str, nome_campus: str):
        nome_campus = nome_campus.lower()
        if not nome_campus in self.campus:
            print("esse campus não foi cadastrado aqui ainda.")
            return
        if not nome_curso in self.campus[nome_campus]:
            print("esse curso não foi cadastrado nesse campus.")
            return
        
        self.campus[nome_campus].remove(nome_curso)
        print(f"o curso {nome_curso} foi removido do campus {nome_campus}.")
        
        
    def atualizar_campus(self, campus: str, novo_nome_campus: str):
        campus = campus.lower()
        if not campus in self.campus:
            print("esse campus não foi cadastrado aqui ainda.")
            return
        self.campus[novo_nome_campus] = self.campus.pop(campus)
        print(f"o campus {campus} foi atualizado para {novo_nome_campus}.")
        
    
    def atualizar_curso_campus(self, curso, nome_campus: str, novo_nome_curso: str):
        nome_campus = nome_campus.lower()
        if not nome_campus in self.campus:
            print("esse campus não foi cadastrado aqui ainda.")
            return
        if not curso in self.campus[nome_campus]:
            print("esse curso não foi cadastrado nesse campus.")
            return
        
        indice = self.campus[nome_campus].index(curso) # o uso do index aqui foi completamente interessante
        self.campus[nome_campus][indice] = novo_nome_curso
        print(f"o curso {curso} foi atualizado para {novo_nome_curso} no campus {nome_campus}.")
    
def menu():
    while True:
        print(" --campus UFC-- ")
        print("1 - Cadastrar Campus")
        print("2 - Cadastrar Curso em Campus")
        print("3 - Verificar os Campus e Cursos")
        print("4 - Remover Campus")
        print("5 - Remover Curso de Campus")
        print("6 - Atualizar Campus")
        print("7 - Atualizar Curso de Campus")
        print("0 - Sair")
    
        opcao = input("escolha uma opcao: ")
        if opcao == "0":
            print("obrigado por não testar, tenha um belo dia.")
            break
        elif opcao == "1":
            nome_campus = input("Digite o nome do campus a ser cadastrado: ")
            ufc.cadastrar_campus(nome_campus)
        elif opcao == "2":
            nome_campus =  input("Digite o nome do campus onde deseja adicionar o curso: ")
            curso_novo = input("Digite o nome do curso a ser adicionado: ")
            ufc.cadastrar_curso_campus(nome_campus, curso_novo)
        elif opcao == "3":
            ufc.verificar_os_campus()
        elif opcao == "4":
            nome_campus = input("Digite o nome do campus a ser removido: ")
            ufc.remover_campus(nome_campus)
        elif opcao == "5":
            nome_curso = input("Digite o nome do curso a ser removido: ")
            nome_campus = input("Digite o nome do campus de onde deseja remover o curso: ")
            ufc.remover_curso_campus(nome_curso, nome_campus)
        elif opcao == "6":
            nome_campus = input("Digite o nome do campus a ser atualizado: ")
            novo_nome_campus = input("Digite o novo nome do campus: ")
            ufc.atualizar_campus(nome_campus, novo_nome_campus)
        elif opcao == "7":
            nome_campus = input("Digite o nome do campus onde deseja atualizar o curso: ")
            nome_curso = input("Digite o nome do curso a ser atualizado: ")
            novo_nome_curso = input("Digite o novo nome do curso: ")
            ufc.atualizar_curso_campus(nome_curso, nome_campus, novo_nome_curso)
        else:
            print("opcao invalida, tente novamente.")
            
print("Bem vindo ao sistema de gerenciamento de campus da UFC!\n")

if __name__ == "__main__":
    ufc = UfcCampus()
    menu()

       