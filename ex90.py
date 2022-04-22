lista = []
for i in range(1, 31):
    lista.append(int(input("digite um número para inserir na lista: ")))
num_pesquisa = int(input("digite o valor que você deseja encontrar na lista: "))
print(lista.count(num_pesquisa))
