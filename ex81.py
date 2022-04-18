q = []
valor = int(input("digite um valor: "))
q.append(valor)
menor = valor
posicao = 0 
for i in range(1, 20):
    valor = int(input("digite um valor: "))
    if valor < menor:
        menor = valor
    q.append(valor)
    posicao = q.index(menor)
print(q, menor, posicao)
