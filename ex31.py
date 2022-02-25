a = float(input("digite um valor: "))
b = float(input("digite um valor: "))
c = float(input("digite um valor: "))

if a < b+c and b < a+c and c < a+b:
    print("esses valores não podem formar um triangulo")
else:
    print("triangulo formado com êxito")
    
