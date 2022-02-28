user = "1234"
password = "9999"
userInput = input("digite o seu usuário: ")
if userInput == user:
    passwordInput = input("Digite a sua senha: ")
    if passwordInput == password:
        print("Acesso permitido")
    else:
        print("senha incorreta")


else:
    print("Usuário inválido!")
