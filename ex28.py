num1 = int(input("digite um número: "))
num2 = int(input("digite um número: "))
num3 = int(input("digite um número: "))
if num2 > num1 and num2 > num3:
    maior = num2
    print(maior)
if num3 > num1 and num3 > num2:
    maior = num3
    print(maior)
if num1 > num2 and num1 > num3:
    maior = num1
    print(maior)
