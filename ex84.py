n = int(input("digite o tamanho da sua lista: "))
a = []
b = []
soma = 0
for i in range(1, n +1):
    a.append(int(input("insira um valor na lista A: ")))
    b.append(int(input("insira um valor na lista B: ")))
    soma = sum(a + b)
print(soma)

    
    
