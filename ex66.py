soma = 0
valor_1 = int(input("digite um valor: "))
valor_2 = int(input("digite um segundo valor: "))
if valor_1 < valor_2:
    for i in range(valor_1, valor_2 + 1):
        soma += i
    print(soma)
    
else:
    for i in range(valor_2, valor_1 + 1):
        soma += i
    print(soma)
    
