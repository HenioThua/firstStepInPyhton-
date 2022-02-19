hora = int(input("digite quantas horas você trabalha por mês: "))
salarioHora = float(input("Quando você ganha por hora? "))
horaExtra = 0.50 * salarioHora
salarioFinal = 0 

if hora > 40:
    salarioFinal = (salarioHora + horaExtra) * hora
    print(salarioFinal)
else:
    salarioFinal = salarioHora * hora
    print(salarioFinal)
    
