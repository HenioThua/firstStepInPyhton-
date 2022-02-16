nota1 = float(input("digite a sua primeira nota: "))
nota2 = float(input("digite a sua segunda nota: "))
mediaFinal = (nota1 + nota2) /2
if mediaFinal >= 6.0:
    print("VOCÊ FOI APROVADO!\nSua média final foi {}".format(mediaFinal))
else:
    print("VOCÊ NÃO FOI APROVADO!\nSua média final foi {}".format(mediaFinal))
