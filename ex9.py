salario = float(input("digite o valor do seu salário :"))
porcentagem = float(input("Porcentagem de reajuste :"))
valor = porcentagem / 100 * salario
novoSalario = salario + valor
print("O novo salário é {}".format(novoSalario))
