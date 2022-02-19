estoqueAtual = int(input("qual a quantidade de produtos que temos no estoque? "))
maximoEstoque = int(input("qual o nosso limite máximo estoque? "))
estoqueMinimo = int(input("qual o nosso limite mínino no estoque? "))
if estoqueAtual >= (maximoEstoque + estoqueMinimo) /2:
    print("NÃO EFETUAR COMPRA")
else:
    print("EFETUAR COMPRA")

