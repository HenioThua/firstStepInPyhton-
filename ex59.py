cont_positivo = 0
cont_negativo = 0
for i in range (1, 11):
    i = int(input("digite um número: "))
    if i >= 0:
        cont_positivo +=1
    else:
        cont_negativo +=1
    print( cont_negativo)
