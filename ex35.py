tipoCombustivel = str.lower(input("Com qual o tipo de combustivel você deseja abastecer o seu carro? (G para gasolina e A para álcool) "))
quantLitros = int(input("quantos litros você deseja? "))
precoA = 2.90
precoG = 3.30
if tipoCombustivel == "a":
    if quantLitros <= 20:
        desconto = (quantLitros * precoA) * 0.03
        total = quantLitros * precoA - desconto
        print("você vai pagar {:.2f}".format(total))
    else:
        desconto = (quantLitros * precoA) * 0.05
        total = quantLitros * precoA - desconto
        print("Você vai pagar {:.2f}".format(total))
else:
    if quantLitros <= 20:
        desconto = (quantLitros * precoG) *0.04
        total = quantLitros * precoG - desconto
        print("Você vai pagar {:.2f}".format(total))
    else:
        desconto = (quantLitros * precoG) *0.06
        total = quantLitros * precoG - desconto
        print("Você vai pagar {:.2f}".format(total))
        
