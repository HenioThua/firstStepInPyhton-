num = int(input("digite um número de 0 até 10: "))
if num > 0 and num < 11:
    for i in range(1, 11):
        multi = num * i
        print(multi)
        i += 1
else:
    print("digite um valor válido na próxima vez")
