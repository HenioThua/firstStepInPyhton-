codigo = int(input("Digite o seu código de usuário: "))
ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_de_entrada_na_empresa = int(input("Digite o ano que você entrou na empresa: "))
if 2022 - ano_de_entrada_na_empresa >= 30:
    print("Requerer aposentadoria")
elif 2022 - ano_nasc >= 65:
    print("Requerer aposentadoria")
elif 2022 - ano_nasc >= 60 and 2022 - ano_de_entrada_na_empresa >= 25:
    print("Requerer aposentadoria")
else:
    print("Não querer")
    
