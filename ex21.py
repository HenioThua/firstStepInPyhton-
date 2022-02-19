horaInicio = int(input("Hora de início: "))
horaFim = int(input("Hora de término: "))
tempoPartida = 0 
if horaInicio > horaFim:
    tempoPartida = horaInicio - horaFim
    print("A partida teve uma duração de {} horas".format(tempoPartida))
else:
    tempoPartida = horaFim - horaInicio
    print("A partida teve uma duração de {} horas".format(tempoPartida))
