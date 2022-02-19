nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura em metros: "))
sexo = str.lower(input("Qual o seu sexo? "))
if sexo == "m":
    pesoIdeal = (72.7 * altura) -58
    print("O peso ideal para você é {:.2f}".format(pesoIdeal))
else:
    pesoIdeal = (62.1 * altura) -44.7
    print("O peso ideal para você é {:.2f}".format(pesoIdeal))
    
