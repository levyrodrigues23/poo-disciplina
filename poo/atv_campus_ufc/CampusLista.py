class UfcCampus:
    def __init__(self):
        self.campus = {} # pensando em usar dicionario para q eu possa armazenar diretamente os cursos em listas
        
    def cadastrar_campus(self, nome_campus: str):
        print("digite no seguinte modelo: Campus do (lugar onde o campus fica, sem os parenteses, é claro)")
        nome_campus = nome_campus.lower()
        
        if nome_campus in self.campus:
            print(f"o campus '{nome_campus}' ja esta cadastrado")
        self.campus[nome_campus] = []
        print(f"o respectivo {nome_campus} foi adicionado ")
        return print(self.campus)
        
    def cursos_campus(self):
        print(f"Aqui estão os respectivos campus e seus cursos\n")
        for i, (chave, valor) in enumerate(self.campus.items()):
            print(f"{i}: Campus: {chave}, Cursos: {[curso for curso in valor]} ")
        
campus = UfcCampus()
campus.cadastrar_campus("Campus do Pici")
campus.cadastrar_campus("campus de Itapaje")
campus.cadastrar_campus("campus de Sobral")
campus.cursos_campus()