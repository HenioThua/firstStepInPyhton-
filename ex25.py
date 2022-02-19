numConta = int(input("Digite o número da sua conta (sem os pontos: "))
saldo = float(input("Digite o seu saldo :"))
debito = float(input("digite o seu débito com o banco: "))
credito = float(input("Digite quanto você tem de crédito com o nosso banco: "))
saldoAtual = saldo - debito + credito
if saldoAtual >= 0:
    print("SALDO POSITIVO")
else:
    print("SALDO NEGATIVO")
