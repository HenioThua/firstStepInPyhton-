q = []
valor = int(input("digite um valor: "))
q.append(valor)
maior = valor
posicao = 0 
for i in range(1, 20):
    valor = int(input("digite um valor: "))
    if valor > maior:
        maior = valor
    q.append(valor)
    posicao = q.index(maior)
print(q, maior, posicao)
