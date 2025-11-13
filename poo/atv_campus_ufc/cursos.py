class Curso:
    def __init__(self):
        self.cursos = []
        
        
    def adicionar_curso(self, curso):
        self.cursos.append(curso)
        print(f"o curso {curso} foi adicionado com sucesso!!!")

    def atualizar_curso(self, curso, nome_atualizado):
        if not curso in self.cursos:
            print("o curso ainda não foi cadastrado, então tecnicamente não tem como atualizar")
        for curso in self.cursos:
            curso = nome_atualizado
            print(f"o curso foi atualizado e agora é assim: {curso}")
            
    def remover_curso(self, curso):
        if not curso in self.cursos:
            print("esse curso não foi cadastrado!")
        for curso in self.cursos:
            self.cursos.pop(curso)
            print(f"o curso {curso} foi completamente removido.")