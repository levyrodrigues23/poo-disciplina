def calculo_esfera(raio: float):
    diametro = 2 * raio
    circunferencia = 2 * 3.14 * raio
    area = 3.14 * raio ** 2
    volume = (4/3) * 3.14 * raio ** 3
    return print("Diâmetro:", diametro, "Circunferência:", circunferencia, "Área:", area, "Volume:", volume)


raio = float(input("Digite o valor do raio: "))
print(calculo_esfera(raio))
    