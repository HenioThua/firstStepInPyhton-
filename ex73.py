habitantes = 0
total_filhos = 0
menor_150 = 0
media_salario_150 = 0 
salario_habitante = float(input("digite o o seu salário: "))
total_salario = salario_habitante
maior_salario = salario_habitante
while salario_habitante > 0:
    numero_filhos = int(input("digite a sua quantidade de filhos: "))
    salario_habitante = float(input("digite o o seu salário: "))
    if maior_salario < salario_habitante:
        maior_salario = salario_habitante
    if salario_habitante <= 150:
        menor_150 += 1
    habitantes += 1
    total_salario += salario_habitante
    total_filhos += numero_filhos
        
media_salario = total_salario / habitantes    
media_filhos =total_filhos // habitantes
media_salario_150 = (menor_150 / habitantes) *100

    
print("Média de salário da população: {}\nMédia do número de filhos: {}\nMaior salário dos habitantes: {}\nPercentual de pessoas com salário menor que R$ 150,00: {}%".format(media_salario, media_filhos, maior_salario, media_salario_150))

        
