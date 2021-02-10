from imagenes import *
from funciones import *
from personajes import *
from items import *


	#Auxiliares



	#Main
print(" ")
print("Bienvenido a la arena soldado")
print("Espero hayas tenido un buen viaje")
print("Nadie de acá es un santo, ¿cuál es especialidad?")
print(" ")

while True:

	print("Elije la clase de tu jugador: ")
	print(" ")
	print("(guerrero) , (mago), (asesino)")

	print(" ")
	print("====================================================================")
	print(" ")

		#Test mode
	#user_input = "mago"

	user_input = input()

	if(user_input == "mago"):
		jugador = Mage()
		print(" ")
		print(jugador.image)
		botR = Warrior()
		botR.name = "trollsen warrior"
		print(" ")
		print("Conque mago eh... espero no seas un creído")
		break

	if(user_input == "asesino"):
		jugador = Rogue()
		print(" ")
		print(jugador.image)
		botR = Mage()
		botR.name = "trollsen mago"
		print(" ")
		print("Conque asesino eh... mejor me cuido la espalda")
		break

	if(user_input == "guerrero"):
		jugador = Warrior()
		print(" ")
		botR = Rogue()
		print(jugador.image)
		botR.name = "trollsen asesino"
		print(" ")
		print("Conque guerrero eh... ¿Un pechopeludo? Jeje")
		break

	print(" ")
	print("No existe la clase: (", user_input, ")")
	print(" ")


print(" ")
print("Y por ciero, un nombre para inscribirte en la arena,")
print("al no ser que quieras que el resto te de uno")
print("Pd: No te lo recomendaria...")
print(" ")

while True:

		#test mode
	#jugador.name = "otis"

	jugador.name = input()

	if (jugador.name == ""):
		print(" ")
		print("...")
		print(" ")
		print("Debes de tener algun nombre, dímelo.")
		print(" ")
		print("====================================================================")
		print(" ")
		continue

	print(" ")
	print("Confirmo entonces, tu nombre es: (", jugador.name, ") ¿verdad?")
	print(" ")
	print("(si), (no)")
	print(" ")

		#Test mode
	#user_input = "si"

	user_input = input()

	if (user_input == "si"):
		print(" ")
		break
	print(" ")
	print("No me tomes el pelo canalla... ¿Cuál es tu nombre?")
	print(" ")
	print("====================================================================")
	print(" ")

print(" ")
print("====================================================================")
print(" ")

print("Bueno, ahora bien")
print("¿Quieres echarte una pelea a ver más si sos")
print("más capaz que el resto de estos idiotas?")
print("¿O quisieras descansar y dejar el entrenamiento para luego?")
print(" ")
print("(batalla), (descansar)")

print(" ")
print("====================================================================")
print(" ")


while True:

		#Test mode
	#user_input = "descansar"

	user_input = input()

	if(user_input == "batalla"):
		battleStart(jugador,botR)
		break

	if (user_input == "descansar"):
		print(" ")
		print("Descansas...")
		jugador.rest()
		print(" ")
		print("====================================================================")
		print(" ")		
		break

	if (user_input == "exit"):
		print(" ")
		print("====================================================================")
		print(" ")		
		break

	print(" . . . ")
	print(" ")
	print("====================================================================")
	print(" ")

while True:
		#Lobby/ciudad
	lobbyText()

	while True:
		print(" ")
		print("====================================================================")
		print(" ")
		print("Defina su acción")
		print(" ")
		print("(buscar batalla) , (armeria), (descansar)")
		print(" ")

			#Test mode
		#user_input = "buscar batalla"

		user_input = input()

		if (user_input == "buscar batalla"):
			print(" ")
			print("Buscando batalla...")
			print(" ")
			print("====================================================================")
			print(" ")
			botR = createBot()
			battleStart(jugador,botR)
			break

		if (user_input == "armeria"):
			print(" ")
			print("====================================================================")
			print(" ")
			armory(jugador)
			lobbyText()

		if (user_input == "descansar"):
			print(" ")
			print("====================================================================")
			print(" ")
			print("Descansas...")
			jugador.rest()
			lobbyText()

		if (user_input == "exit"):
			print(" ")
			print("====================================================================")
			print(" ")		
			break


	if (user_input == "exit"):
		break
