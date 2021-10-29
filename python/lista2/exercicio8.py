numeroEleitoresMunicipio = int(input("Insira o numero de eleitores do municipio: "))
numeroVotosBrancos = int(input("Insira o numero de votos brancos: "))
numeroVotosNulos = int(input("Insira o numero de votos nulos: "))
numeroVotosValidos = int(input("Insira o numero de votos validos: "))

print("A porcentagem de numero de votos brancos é:", str((numeroVotosBrancos/numeroEleitoresMunicipio)*100) + "%")
print("A porcentagem de numero de votos nulos é:", str((numeroVotosNulos/numeroEleitoresMunicipio)*100) + "%")
print("A porcentagem de numero de votos validos é:", str((numeroVotosValidos/numeroEleitoresMunicipio)*100) + "%")
