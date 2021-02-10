	#Archivos importados
from imagenes import *
from personajes import *
from items import *

import random

def randomIntAttack():
	x = int
	x = random.randint(0,100)
	
	return x

def randomIntCreate():
	x = int
	x = random.randint(0,2)
	
	return x

def createBot():
	x = randomIntCreate()
	if (x == 0):
		bot = Mage()
		bot.name = "trollsen mago"
	if (x == 1):
		bot = Warrior()
		bot.name = "trollsen guerrero"
	if (x == 2):
		bot = Rogue()
		bot.name = "trollsen asesino"

	return bot

def IA(bot, jugador, frapStatic, frapBasic):
	while True:
		if (bot.image == mageIm):
			nRandom = randomIntAttack()
			if (nRandom >= 50):
				if (bot.stamina < 1):
					continue
				bot.basicAttack(jugador)
				print(bot.name," Uso: ", "Ataque basico")
				print(" ")
				print(" you ")
				print(frapBasic)
				break
			if (nRandom >= 25):
				if (bot.mana < 25):
					if (bot.stamina < 3):
						continue
					continue
				bot.fireBall(jugador)
				print(bot.name," Uso: ", "Bola de fuego")
				print(" ")
				print(" you ")
				print(frapBasic)
				break
			if (nRandom >= 0):
				bot.pasar()
				print(bot.name," Uso: ", "Pasar")
				print(" ")
				print(" you ")
				print(frapStatic)
				break

		if (bot.image == warriorIm):
			nRandom = randomIntAttack()
			if (nRandom >= 50):
				if (bot.stamina < 1):
					continue
				bot.basicAttack(jugador)
				print(bot.name," Uso: ","Ataque basico")
				print(" ")
				print(" you ")
				print(frapBasic)
				break
			if (nRandom >= 25):
				if (bot.stamina < 6):
					continue
				bot.porrazo(jugador)
				print(bot.name," Uso: ", "Porrazo")
				print(" ")
				print(" you ")
				print(frapBasic)
				break
			if (nRandom >= 0):
				bot.pasar()
				print(bot.name," Uso: ", "Pasar")
				print(" ")
				print("you ")
				print(frapStatic)
				break

		if (bot.image == rogueIm):
			nRandom = randomIntAttack()
			if (nRandom >= 50):
				if (bot.stamina < 1):
					continue
				bot.basicAttack(jugador)
				print(bot.name," Uso: ", "Ataque basico")
				print(" ")
				print("you ")
				print(frapBasic)
				break
			if (nRandom >= 25):
				if (bot.stamina < 4):
					continue
				bot.poison(jugador)
				print(bot.name," Uso: ", "Envenenar")
				print(" ")
				print(" you ")
				print(frapBasic)
				break
			if (nRandom >= 0):
				bot.pasar()
				print(bot.name," Uso: ", "Pasar")
				print(" ")
				print("you ")
				print(frapStatic)
				break

def getStats(jugador, bot):
	print(jugador.name, ":")
	print("hp = ", jugador.hp)
	print("mana = ", jugador.mana)
	print("stamina = " ,jugador.stamina)
	print("intelect = " ,jugador.intelect)
	print("strength = ", jugador.strength)

	print(" ")

	print(bot.name, ":")
	print("hp = ", bot.hp)
	print("mana = ", bot.mana)
	print("stamina = " ,bot.stamina)
	print("intelect = ", bot.intelect)
	print("strength = ", bot.strength)


def getImage(jugador, bot):
	if (jugador.image == mageIm):
		if (bot.image == warriorIm):
			frapStatic = mageVsWarriorIm
		if (bot.image == rogueIm):
			frapStatic = mageVsRogueIm
		if (bot.image == mageIm):
			frapStatic = mageVsMageIm

	if (jugador.image == rogueIm):
		if (bot.image == mageIm):
			frapStatic = rogueVsMageIm
		if (bot.image == warriorIm):
			frapStatic = rogueVsWarriorIm
		if (bot.image == rogueIm):
			frapStatic = rogueVsRogueIm

	if (jugador.image == warriorIm):
		if (bot.image == rogueIm):
			frapStatic = warriorVsRogueIm
		if (bot.image == mageIm):
			frapStatic = warriorVsMageIm
		if (bot.image == warriorIm):
			frapStatic = warriorVsWarriorIm

	if (frapStatic == mageVsWarriorIm):
		frapBasic = mageVsWarriorBasicAIm

	if (frapStatic == mageVsRogueIm):
		frapBasic = mageVsRogueBasicAIm

	if (frapStatic == mageVsMageIm):
		frapBasic = mageVsMageBasicAIm

	if (frapStatic == rogueVsMageIm):
		frapBasic = rogueVsMageBasicAIm

	if (frapStatic == rogueVsWarriorIm):
		frapBasic = rogueVsWarriorBasicAIm

	if (frapStatic == rogueVsRogueIm):
		frapBasic = rogueVsRogueBasicAIm

	if (frapStatic == warriorVsMageIm):
		frapBasic = warriorVsMageBasicAIm

	if (frapStatic == warriorVsRogueIm):
		frapBasic = warriorVsRogueBasicAIm

	if (frapStatic == warriorVsWarriorIm):
		frapBasic = warriorVsWarriorBasicAIm

	return frapStatic, frapBasic

	#Función batalla
def battleStart(jugador, bot):
	turn = 1
	frapStatic, frapBasic = getImage(jugador, bot)
	print(" ")
	print("====================================================================")
	print(" ")
	print("Comienzas una batalla...")
	print("Tu oponente es: ", bot.name)
	print(" ")
	print("you ")
	print(frapStatic)
	getStats(jugador, bot)

		#Comienzo de la batalla
	while True is True:

		while True is True:
			print("====================================================================")
			print("Turno: ", turn)
			print("====================================================================")
			print("Tu turno...")
			print("====================================================================")
			print("Defina su acción")
			print(" ")
			print(" ")
			print("Habilidades básicas:  ", jugador.basic_abilities)
			print("Habilidades de clase: ", jugador.class_abilities)
			print("Inventario: ", jugador.inventory)
			print(" ")
			user_input = input()
			print(" ")

			if (user_input == "golpe basico"):
				if (jugador.stamina >= 1): 
					jugador.basicAttack(bot)

					print(" you")
					print(frapBasic)
					getStats(jugador, bot)

					break

				print("No tienes estamina suficiente")

			
			if (user_input == "bola de fuego"):
				if ("bola de fuego" in jugador.class_abilities):
					if (jugador.mana >= 25 and jugador.stamina >= 3):
						jugador.fireBall(bot)

						print(" you")		
						print(frapBasic)
						getStats(jugador, bot)

						break

					print(" ")
					print("No tienes maná suficiente")
					continue

				print(" ")
				print ("No conoces esa magia...")

			if (user_input == "porrazo"):
				if ("porrazo" in jugador.class_abilities):
					if (jugador.stamina >= 5):
						jugador.porrazo(bot)

						print(" you")		
						print(frapBasic)
						getStats(jugador, bot)

						break

					print(" ")
					print("No tienes estamina suficiente")
					continue

				print(" ")
				print ("No conoces ese movimiento...")

			if (user_input == "envenenar"):
				if ("envenenar" in jugador.class_abilities):
					if (jugador.stamina >= 4):
						jugador.poison(bot)

						print(" you")		
						print(frapBasic)
						getStats(jugador, bot)

						break

					print(" ")
					print("No tienes estamina suficiente")
					continue

				print(" ")
				print("No conoces ese movimiento...")

			if (user_input == "pocion de vida"):
				if("pocion de vida" in jugador.inventory):
					jugador.drinkHealthPotion()
					jugador.inventory.remove("pocion de vida")
					print(" ")
					print("Bebes una poción de vida...")
					print(" ")
					print("you")
					print(frapStatic)
					getStats(jugador, bot)

					break

				print(" ")
				print("No tienes una poción de vida en tu inventario...")
				print(" ")

			if (user_input == "pocion de mana"):
				if("pocion de mana" in jugador.inventory):
					jugador.drinkManaPotion()
					jugador.inventory.remove("pocion de mana")
					print(" ")
					print("Bebes una poción de mana...")
					print(" ")
					print("you")
					print(frapStatic)
					getStats(jugador, bot)

					break

				print(" ")
				print("No tienes una poción de mana en tu inventario...")
				print(" ")

			if (user_input == "pocion de estamina"):
				if("pocion de vida" in jugador.inventory):
					jugador.drinkStaminaPotion()
					jugador.inventory.remove("pocion de estamina")
					print(" ")
					print("Bebes una poción de estamina...")
					print(" ")
					print("you")
					print(frapStatic)
					getStats(jugador, bot)

					break

				print(" ")
				print("No tienes una poción de estamina en tu inventario...")
				print(" ")


			if (user_input == "pasar"):
				jugador.pasar()
				print(" ")
				print("Pasas de turno...")
				print(" ")
				print("you")
				print(frapStatic)
				getStats(jugador, bot)

				break

			if (user_input == "exit"):
				break

		if (user_input == "exit"):
			break

		if(bot.poisoned > 0):
			bot.poisonDamage()
			if (bot.hp <= 0):
				print(" ")
				print("Muerte por envenenamiento...")
				print(" ")
				print("you")
				print(frapStatic)
				getStats(jugador, bot)

		if (bot.hp <= 0):
			del bot
			print(" ")
			print("¡Has ganado la batalla!")
			print(" ")
			print("====================================================================")
			print(" ")
			break

		print(" ")
		print("====================================================================")
		print(" Turno del oponente...")
		print("====================================================================")
		print(" ")
	

		IA(bot, jugador, frapStatic, frapBasic)

		getStats(jugador, bot)

		if (jugador.poisoned > 0):
			jugador.poisonDamage()

		if (jugador.hp <= 0):
			print(" ")
			print("====================================================================")
			print(" ")
			print("Has muerto...")
			print(" ")
			print("====================================================================")
			print(" ")
			while True is True:
				pass

		turn += 1
				
def lobbyText():
	print("Bienvenido a la ciudad, desde acá podés:")
	print(" ")
	print("Buscar una pelea en la arena")
	print(" ")
	print("Descansar para recuperar tus puntos de salud")
	print(" ")
	print("Ten en cuenta si has batallado ya que necesitas descansar")
	print("para recuperar tus puntos de salud")


def armoryText():
	print("Bienvenido a la armería, ¿qué querés comprar?")
	print(" ")
	print("(pocion de vida), (pocion de mana), (pocion de estamina), (salir)")
	print(" ")

def armory(player):

	armoryText()

	while True:
		user_input = input()

		if (user_input == "pocion de vida"):
			player.inventory.append("pocion de vida")
			print(" ")
			print("Gracias por comprar una poción de vida")
			print("nunca están de más...")
			print(" ")

		if (user_input == "pocion de mana"):
			player.inventory.append("pocion de mana")
			print(" ")
			print("Gracias por comprar una poción de mana")
			print("para mantenerte completo eh...")
			print(" ")


		if (user_input == "pocion de estamina"):
			player.inventory.append("pocion de estamina")
			print(" ")
			print("Gracias por comprar una poción de estamina")
			print("a veces nos salvan las papas...")
			print(" ")

		if(user_input == "salir"):
			print(" ")
			print("====================================================================")
			print(" ")
			break

		if (user_input == "exit"):
			print(" ")
			print("====================================================================")
			print(" ")		
			break

		print("¿Acaso deseas algo más?")
		print(" ")
		print("====================================================================")
		print(" ")
		print("(pocion de vida), (pocion de mana), (pocion de estamina), (salir)")
		print(" ")