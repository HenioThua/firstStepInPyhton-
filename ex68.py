valor_total = 0
media_preco = 0 
numero_pecas = int(input("digite o número de peças em estoque: "))
for i in range (numero_pecas):
    valor_peca = float(input("digite o valor da peça: "))
    valor_total += valor_peca
media_preco = valor_total / numero_pecas
print("o valor total das peças é {:.2f} e a media de preços é {:.2f}".format(valor_total, media_preco))
