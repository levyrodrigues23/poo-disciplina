import math

def exibir_perimetro(raio):
    perimetro = 2 * math.pi * raio
    return print(f"o perimetro da sua circunferencia equivale a {perimetro}")

raio = float(input("digite o valor do raio da sua circunferencia:"))
exibir_perimetro(raio)