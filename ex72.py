preco_total = 0
maior_preco = 0
media_precos = 0 
for i in range(5):
    codigo = int(input("digite o codigo do produto: "))
    preco_produto = float(input("Digite o preço do produto:".format(codigo)))
    if maior_preco < preco_produto:
        maior_preco = preco_produto
    preco_total += preco_produto
    media_precos = preco_total / 5
print(media_precos)
    
    
    
