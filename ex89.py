lista_1 = []
lista_2 = []
for i in range (1,16):
    lista_1.append(int(input("digite um número para inserir na lista 1: ")))
    lista_2.append(int(input("digite um número para inserir na lista 2: ")))
print("elementos em comum", set(lista_1) & set(lista_2))
