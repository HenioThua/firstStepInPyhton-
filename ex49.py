nota_1 = int(input("Digite a sua primeira nota: "))
nota_2 = int(input("Digite a sua segunda nota: "))
nota_final = 0
novo_calculo = "S"
while novo_calculo == "S":
    nota_1 = int(input("Digite a sua primeira nota: "))
    nota_2 = int(input("Digite a sua segunda nota: "))
    while nota_1 < 0:
        nota_1 = int(input("Digite a sua primeira nota: "))   
    while nota_1 > 10:
        nota_1 = int(input("Digite a sua primeira nota: "))
        
    while nota_2 < 0:
        nota_2 = int(input("Digite a sua segunda nota: "))
    while nota_2 > 10:
        nota_2 = int(input("Digite a sua segunda nota: "))
    nota_final = (nota_1 + nota_2) / 2
    print(nota_final)
    novo_calculo = str.upper(input("Digite S para fazer um novo cálculo e N para terminar o programa: "))
