homem1 = int(input("Digite a sua idade: "))
homem2 = int(input("Digite a sua idade: "))
mulher1 = int(input("Digite a sua idade: "))
mulher2 = int(input("digite a sua idade: "))
maior = homem1
menor = homem1
if homem2 > homem1:
    maior = homem2
if homem2 < homem1:
    menor = homem2

maiorM = mulher1
menorM = mulher1

if mulher2 > mulher1:
    maiorM = mulher2
if mulher2 < mulher1:
    menorM = mulher2

somaIdade1 = maior + menorM
somaIdade2 = menor + maiorM

print(" A soma das idades do homem mais velho com a muulher mais nova é {}".format(somaIdade1))
print(" A soma das idades da mulher mais velha com o homem mais novo é {}".format(somaIdade2))
