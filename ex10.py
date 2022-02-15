valorInicialCarro = float(input("valor inicial do carro: "))
percentualDistri = valorInicialCarro * 0.28
percentualImposto = valorInicialCarro * 0.45
valorFinalCarro = valorInicialCarro + percentualDistri + percentualImposto
print("O carro vai sair por {} R$".format(valorFinalCarro))
