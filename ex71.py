soma = 0
media = 0
maior = 0
quantidade_elementos = int(input("Digite uma quantidade: "))
maximo_elementos = quantidade_elementos
for i in range (quantidade_elementos):
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
    soma += valor
media = soma / quantidade_elementos
print(maior, media)
    
