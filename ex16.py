preco1 = 1.30
preco2 = 1.00
quant= int(input("Quantas maças você deseja levar? "))
if quant >= 12:
    valor = quant * preco2
    print("Você vai pagar {} R$ reais".format(valor))
else:
    valor = quant * preco1
    print("você vai pagar {} R$ reais".format(valor))
