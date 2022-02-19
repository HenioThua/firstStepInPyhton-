salarioFixo = float(input("qual o seu salário fixo? "))
vendas = float(input("quanto você teve em vendas? "))
if vendas <= 1500:
    porcent = vendas * 0.03
    salarioFixo += porcent
    print("O seu salário é ", salarioFixo)
else:
    porcent = vendas * 0.05
    salarioFixo += porcent
    print("O seu salário é ", salarioFixo)
