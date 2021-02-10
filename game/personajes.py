from imagenes import *

	#Personajes
class Characters():
	name = str
	max_hp = int
	hp = int
	max_mana = int
	mana = int
	max_stamina = int
	stamina = int
	intelect = int
	strength = int
	image = str
	basic_abilities = ["golpe basico" , "pasar"]
	class_abilities = []
	inventory = []
	poisoned = 0

	def basicAttack(self, enemy):
		self.stamina -= 1
		enemy.hp -= self.strength

	def pasar(self):
		self.stamina +=  3
		if (self.stamina > self.max_stamina):
			self.stamina = self.max_stamina

	def poisonDamage(self):
		self.hp -= self.poisoned
		self.poisoned -= 1

	def drinkHealthPotion(self):
		self.hp += int(self.max_hp / 3)

		if (self.image == mageIm):
			if (self.hp > self.max_hp):
				self.hp = self.max_hp

		if (self.image == warriorIm):
			if (self.hp > self.max_hp):
				self.hp = self.max_hp

		if (self.image == rogueIm):
			if (self.hp > self.max_hp):
				self.hp = self.max_hp

	def drinkManaPotion(self):
		self.mana += int(self.max_mana / 3)

		if (self.image == mageIm):
			if (self.mana > self.max_mana):
				self.mana = self.max_mana

		if (self.image == warriorIm):
			if (self.mana > self.max_mana):
				self.mana = self.max_mana

		if (self.image == rogueIm):
			if (self.mana > self.max_mana):
				self.mana = self.max_mana

	def drinkStaminaPotion(self):
		self.stamina += int(self.max_stamina / 2)

		if (self.image == mageIm):
			if (self.stamina > self.max_stamina):
				self.stamina = self.max_stamina

		if (self.image == warriorIm):
			if (self.stamina > self.max_stamina):
				self.stamina = self.max_stamina

		if (self.image == rogueIm):
			if (self.stamina > self.max_stamina):
				self.stamina = self.max_stamina

	#Clase mago
class Mage(Characters):
	max_hp = 50
	hp = 50
	max_mana = 100
	mana = 100
	max_stamina = 10
	stamina = 10
	intelect = 10
	strength = 1
	image = mageIm
	class_abilities = ["bola de fuego"]

	def rest(self):
		self.hp = 50
		self.mana = 100
		self.stamina = 10
		self.intelect = 10
		self.strength = 1

	def fireBall(self, enemy):
		self.mana -= 25
		self.stamina -= 3
		enemy.hp -= (self.intelect * 4)

	#Clase guerrero
class Warrior(Characters):
	max_hp = 100
	hp = 100
	max_mana = 0
	mana = 0
	max_stamina = 10
	stamina = 10
	intelect = 1
	strength = 6
	image = warriorIm
	class_abilities = ["porrazo"]

	def rest(self):
		self.hp = 100
		self.mana = 0
		self.stamina = 10
		self.intelect = 1
		self.strength = 6

	def porrazo(self, enemy):
		self.stamina -= 6
		enemy.hp -= int((enemy.hp / 2))

	#Clase asesino
class Rogue(Characters):
	max_hp = 65
	hp = 65
	max_mana = 25
	mana = 25
	max_stamina = 10
	stamina = 10
	intelect = 3
	strength = 4
	image = rogueIm
	class_abilities = ["envenenar"]

	def rest(self):
		self.hp = 65
		self.mana = 25
		self.stamina = 10
		self.intelect = 3
		self.strength = 4

	def poison(self, enemy):
		self.stamina -= 4
		enemy.poisoned += 5
