nota_1 = float(input("Digite a sua primeira nota: "))
nota_2 = float(input("Digite a sua segunda nota: "))
nota_3 = float(input("Digite a sua terceira nota: "))
media_dos_exercicios = float(input("digite a Média dos seus Exercícios: "))
media_final = (nota_1 + nota_2 *2 + nota_3 * 3 +  media_dos_exercicios) / 7
if media_final > 9.0:
    print("O seu conceito de nota foi: A!")   
if media_final >= 7.5 and media_final < 9.0:
    print("O seu conceito de nota foi: B!")
    
if media_final >= 6.0 and media_final < 7.5:
    print("O seu conceito de nota foi: C!")

if media_final < 6.0:
    print("O seu conceito de nota foi: D!")
