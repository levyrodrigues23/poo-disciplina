def pagamento_semanal(salario_hora, horas_regulares, horas_extras):
    pagamento = salario_hora * horas_regulares + horas_extras * (salario_hora * 1.5)
    return pagamento




salario_hora = float(input("digite o valor do salario por hora:"))
horas_regulares = float(input("digite a quantidade de horas trabalhadas no mês:"))
horas_extras = float(input("digite a quantidade de horas extras trabalhadas no mês:"))
print(f"o pagamento semanal é de: R${pagamento_semanal(salario_hora, horas_regulares, horas_extras)}")