import math 

def calcular_distancia(x1, y1, x2, y2):
   
   
    distancia_euclidiana = math.sqrt((x2 - x1) ** 2 +  (y2 - y1) ** 2)
    return print(f"a distancia entre os dois pontos que voce digitou equivalem a {distancia_euclidiana}")  


x1 = float(input("digite o valor de x1: "))
y1 = float(input("digite o valor de y1: "))
x2 = float(input("digite o valor de x2: "))
y2 = float(input("digite o valor de y2: "))

calcular_distancia(x1, y1, x2, y2)