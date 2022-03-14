valor_total = 0
cont = 0
media_preco = 0
resposta = str.lower(input("MAIS MERCADORIAS (S/N): "))
while resposta == "s":
    valor_peca = float(input("qual o valor da peça: "))
    resposta = str.lower(input("‘MAIS MERCADORIAS (S/N)"))
    valor_total += valor_peca
    cont += 1
media_preco = valor_total / cont
print("O valor total é {} e a media de preços é {}".format(valor_total, media_preco))

    
