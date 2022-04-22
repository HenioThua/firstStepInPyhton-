temperatura_ano = []
temp = int(input("qual a temperatura? ")) 
maior_temp = temp
menor_temp = maior_temp
cont_dias = 1
temperatura_ano.append(temp)
media_temp = temperatura_ano
cont_dias_inferior = 0 
for i in range(1,3):
    temp = int(input("qual a temperatura? "))
    temperatura_ano.append(temp)
    if temp > maior_temp:
        maior_temp = temp
    if temp < menor_temp:
        menor_temp = temp
    cont_dias += 1
    media_temp = sum(temperatura_ano) / cont_dias
    if temp < media_temp:
        cont_dias_inferior += 1
print(media_temp, maior_temp, menor_temp, cont_dias_inferior)
    
