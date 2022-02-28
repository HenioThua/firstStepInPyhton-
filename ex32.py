timeA = input("Digite o nome do primeiro time: ")
timeB = input("digite o nome do segundo time: ")
golsA = int(input("quantos gols o {} marcou? ".format(timeA)))
golsB = int(input("quantos gols o {} marcou? ".format(timeB)))
if golsA == golsB:
    print("O jogo terminou com empate")
elif golsA > golsB:
    print("o time vencedor foi {}".format(timeA))
else:
    print("O time vencedor foi {}".format(timeB))
