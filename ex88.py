lista = []
for i in range(1,21):
    lista.append(int(input("digite um valor para ser inserido na lista: ")))
num_pesquisa = int(input("digite um número: "))
if num_pesquisa in lista:
    posicao = lista.index(num_pesquisa)
    del(lista[posicao])
    print(lista)
else:
    print("esse elemento não está contido na lista")
