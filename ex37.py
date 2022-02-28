quilosMaca = float(input("Quantos quilos de maça você vai levar? "))
quilosMorango = float(input("Quantos quilos de morango você vai levar? "))
quilosTotal = quilosMaca + quilosMorango

if quilosTotal <= 5:
    totalMaca = quilosMaca * 1.80
    totalMorango = quilosMorango * 2.50
    valorTotal = totalMaca + totalMorango
    print("Você vai pagar {:.2f}".format(valorTotal))

elif quilosTotal > 5:
    totalMaca = quilosMaca * 1.50
    totalMorango = quilosMorango * 2.20
    valorTotal = totalMaca + totalMorango
    if quilosTotal > 5 and valorTotal > 25:
        desconto = valorTotal * 0.10
        valorTotal = valorTotal - desconto
        print("Você vai pagar {:.2f}".format(valorTotal))
    else:
        print("Você vai pagar {:.2f}".format(valorTotal))
