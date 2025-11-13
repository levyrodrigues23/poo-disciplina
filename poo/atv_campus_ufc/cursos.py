class Curso:
    def __init__(self):
        self.cursos = []
        
        
    def adicionar_curso(self, curso: str):
        print(f"o curso {curso} foi adicionado com sucesso.")
        return self.cursos.append(curso)

        

    def atualizar_curso(self, curso: str, nome_atualizado: str):
        if not curso in self.cursos:
            print("o curso ainda não foi cadastrado, então tecnicamente não tem como atualizar")
        for indice, nome_curso in enumerate(self.cursos):
            if nome_curso == curso:
                self.cursos[indice] = nome_atualizado       
                print(f"o curso {curso} foi atualizado para {nome_atualizado}")         
                
                
            
    def remover_curso(self, curso: str):
        if not curso in self.cursos:
            print("esse curso não foi cadastrado!")
        for i in self.cursos:
            if i == curso:
                print(f"o curso {curso} foi completamente removido.")
                return self.cursos.remove(curso)
                
                
            
    def verificar_curso(self, curso):
        print(self.cursos)
        if not curso in self.cursos:
            print("o curso que voce digitou não consta cadastramento.")
        for i in self.cursos:
            if i == curso:
                print(f"o curso {curso} existe")
                
# vou testar aqui pra ver se realmente ta funcionando ou se eu fiz errado, senão eu vou ter que corrigir miseravelmente

curso = Curso()


curso.atualizar_curso("medicina", "medicina veterinaria")
curso.remover_curso("medicina")
curso.remover_curso("medicina veterinaria")
curso.verificar_curso("medicina")
curso.adicionar_curso("medicina")
curso.verificar_curso("medicina veterinaria")
curso.verificar_curso("medicina")

# atualmente pelo que vejo está funcionando normalmente, isso é realmente bom