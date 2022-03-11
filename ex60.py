cont_primario = 0
cont_secundario = 0 
for i in range(1, 11):
    valor = int(input("Digite um valor: "))
    if valor >= 10 and valor <=20:
        cont_primario += 1
    else:
        cont_secundario += 1
print("A quantidade de números entre 10 e 20 é {} e os que estão fora disso são {}".format(cont_primario, cont_secundario))
