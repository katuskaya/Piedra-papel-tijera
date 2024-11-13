nombre1 = input("como se llamara el jugador1: ")
nombre2 = input("como se llamara el jugador2: ")


Jugador1 = input("Hola Jugador1 Que eliges? Piedra,papel o tijeras?: ")
Jugador2 = input("Hola Jugador2 Que eliges? Piedra,papel o tijeras?: ")

condicion1 = Jugador1 == "piedra" and Jugador2 == "tijeras"
condicion2 = Jugador1 == "papel" and Jugador2 == "piedra"
condicion3 = Jugador1 == "tijeras" and Jugador2 == "papel"


if Jugador1 == Jugador2:
    print( "Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print ("Ha ganado el jugador 1", nombre1)
else:
    print ("Ha ganador el jugador 2", nombre2)

