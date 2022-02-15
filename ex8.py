brancos = int(input("Quantidade de votos em brancos: "))
nulos = int(input("Quantidade de votos nulos: "))
validos = int(input("Quantidade de votos validos :"))
eleitores = brancos + nulos + validos 
validosPorcent= validos / eleitores * 100
brancosPorcent= brancos / eleitores * 100
nulosPorcent= nulos / eleitores * 100
print(" ELEITORES {}\n VOTOS EM BRANCO {:.2f}%\n VOTOS NULOS {:.2f}%\n VOTOS VALIDOS {:.2f}%".format(eleitores, brancosPorcent, nulosPorcent, validosPorcent ))



