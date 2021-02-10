class LifePotion():
	name = "pocion de vida"

	def drink(player):
		player.hp += player.max_hp / 3

		if (player.image == mageIm):
			if (player.hp > player.max_hp):
				player.hp = player.max_hp

		if (player.image == warriorIm):
			if (player.hp > player.max_hp):
				player.hp = player.max_hp

		if (player.image == rogueIm):
			if (player.hp > player.max_hp):
				player.hp = player.max_hp