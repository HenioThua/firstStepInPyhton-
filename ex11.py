carrosVendidos = int(input("Quantos carros você vendeu? "))
valorTotaldeVendas = float(input("Qual o valor total da suas vendas? "))
salarioFixo = float(input("Qual o seu salário fixo? "))
valorExtraPorCarro = float(input("Quanto você recebe de comissão por carro vendido? "))
comissaoVendas = valorTotaldeVendas * 0.05
comissaoCarros = valorExtraPorCarro * carrosVendidos
salarioFinal = comissaoVendas + comissaoCarros + salarioFixo
print("O seu salário final é de {} R$".format(salarioFinal))
