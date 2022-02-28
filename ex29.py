num1 = int(input("digite um número: "))
num2 = int(input("digite um número: "))
num3 = int(input("digite um número: "))
if num1 > num2 and num1 > num3:
    maior = num1
    print(maior)
    
if num2 > num1 and num2 > num3:
    maior = num2
    print(maior)
    
if num3 > num1 and num3 > num2:
    maior = num3
    print(maior)

#######SEGUNDO MAIOR#######

if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
    segundoMaior = num1 
    print(segundoMaior)

if num2 > num1 and num2 < num3 or num2 > num3 and num2 < num1:
    segundoMaior = num2
    print(segundoMaior)

if num3 > num1 and num3 < num2 or num3 > num2 and num3 < num1:
    segundoMaior = num3
    print(segundoMaior)

print("A soma é {}".format(maior + segundoMaior))
    



