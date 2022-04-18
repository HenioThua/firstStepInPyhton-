a = []
valor = 0
lista_invertida = []
for i in range(1,21):
    valor = int(input("Digite um valor para a lista: "))
    a.append(valor)
    lista_invertida = a[::-1]
print(lista_invertida)
