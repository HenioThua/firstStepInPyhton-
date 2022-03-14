maior = 0
menor = 0
maximo_elementos = 100
valor = int(input("Digite um valor: "))
maior = valor
menor = valor
for i in range (maximo_elementos - 1):
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor     
print(maior, menor)
    
