nomeProduto = input("Digite o nome do produto: ")
quantProduto = int(input("Digite a quantidade do produto: "))
precoProduto = float(input("Digite o valor de cada produto: "))
total = quantProduto * precoProduto
if quantProduto <= 5:
    desconto = total * 0.02
    totalFinal = total - desconto
    print("O valor total foi {} e você teve um desconto de {}".format(totalFinal, desconto))
elif quantProduto > 5 and quantProduto <= 10:
    desconto = total * 0.03
    totalFinal = total - desconto
    print("O valor total foi {} e você teve um desconto de {}".format(totalFinal, desconto))
elif quantProduto > 10:
        desconto = total * 0.05
        totalFinal = total - desconto
        print("O valor total foi {} e você teve um desconto de {}".format(totalFinal, desconto))

