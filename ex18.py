anoAtual = int(input("Digite o ano ATUAL: "))
anoNasc = int(input("Digite o ano do seu NASCIMENTO: "))
idade = anoAtual - anoNasc
if idade >= 16:
    print("Vocẽ poderá votar esse ano.")
else:
    print("Você ainda não pode votar.")
