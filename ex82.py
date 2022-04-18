a = []
m = []
valor_final = 0
x = int(input("digite um multiplicador: "))
for i in range(1,11):
    valor = int(input("digite um valor para a lista: "))
    a.append(valor)
    valor_final = valor * x
    m.append(valor_final)
print(m)
