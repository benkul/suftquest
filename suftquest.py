### imports ###
from random import randrange
from random import choice

see = [ # create a list of words to use so see is not used exclusively, called via choice(see)
"spot",
"see",
"observe",
"notice"
]

adjective_list_size = [ # create a list of adjectives that can be used to give any statement size-related variety via choice(adjective_list_size)
"tiny ",
"large ",
"diminutive ",
"big ",
"huge ",
"small ",
"",""
]
adjective_list_where = [ # create a list of statements that can be used to give locational variety to items in a room via choice(adjective_list_where)
"on a shelf",
"behind the door",
"on the floor",
"wedged between books on a shelf",
"off to the left",
"nearby",
"on your right side",
"on a table",
"in the center of the room",
"at your feet",
"in the far corner"
]

monster_actions = [ 
"sizing you up", 
"glaring at you", 
"waiting for you", 
"examining your gear", 
"licking its lips", 
"salivating earnestly", 
"reading a dusty tome", 
"pondering life",
"contemplating its existence",
"studying for the SAT",
"doing his geometry homework",
"doodling on the walls using blood",
"defecating in the corner",
"bleeding from multiple stab wounds",
"practising Spanish verb conjugations",
"singing operatic overtures, Wagner I think",
"reading a book."
"gnashing its fangs",
"drooling rather excessively",
"trolling internet forums",
"conducting necraphagic funeral rituals",
"eating its breakfast"
]

empty_rooms = [
"The room is quite empty",
"There is nothing worth looting here",
"The only thing worth noting in the room is your breath, which is foul",
"It's kind of empty in this room",
"There is nothing here of interest",
"No chests, no potions, no monsters, no fun to be had here",
]

adjective = [
"brick-walled", 
"cavernous", 
"dark and musty", 
"dim and musty", 
"huge", 
"tiny", 
"small", 
"damp", 
"well-lit", 
"dimly-lit", 
"musty", 
"dank", 
"dark", 
"wood-panelled",
"poorly-lit"
]

sentence = [
"There are bits of bone and detritus on the floor which you can't help but step on as you walk.",
"It smells strongly of cat urine. You hold back the urge to puke.",
"You can hear the sound of rats somewhere nearby and notice their droppings on the floor.",
"Lichen cover the walls and deaden the echo of your footsteps.",
"Light filters in through a hole in the ceiling.",
"Insect husks crunch under your feet as you walk.",
"You're certain you can hear voices coming from the next room, but as you approach they quiet.",
"You feel as if you are being watched and the hairs on the back of your neck stand at attention.",
"The temperature here is warm, a little too warm and you begin to sweat.",
"The floor is sticky, with what you cannot tell.",
"The room is completely silent.  You need to leave quickly, you can feel your nerves fraying.",
"There are bloody footsteps leading to a dead body, you search it but find nothing useful.",
"On the floor you see the skull of an unknown animal.",
"The walls in the room are crumbling away, you need to leave before one of them collapses.",
"You hear your footsteps echoed back strangely, nothing in the room seems to account for this.",
"There are strange goat noises coming from behind the walls. It is unnerving.",
"There is a chill in the air, it is noticeably colder here.",
"Dust covers every surface, nobody has been in this room for ages."
]

weapon_type = [
"axe",
"sword",
"dagger",
"mace",
"spear",
"lance",
]

weapon_prefix = [
"flaming",
"icy",
"bludgeoning",
"massive",
"heavy",
"sharp",
"cursed",
"holy",
"rusted",
"automatic",
"slashing",
"repeating",
"","","",""
]

weapon_suffix = [
"of bloodletting",
"of killing",
"of the nine moons",
"of limitless power",
"of blocking",
"of eternal darkness",
"of final logic",
"of horrible coagulation",
"of the bold", 
"of holy power",
"of the dead",
"of the galaxy",
"of the blinding sun",
"of burning",
"of the pineapple gods",
"","","",""
]

armor_prefixes = [
"rusty ",
"iron ",
"steel ",
"platinum ",
"palladium ",
"dented ",
"dragon ",
"golden ",
"silver ",
"titanium ",
"brass ",
"tin ",
"aluminium ",
"lead ",
"",""
]

armor_head = [
"armet",
"sallet",
"barbute",
"great helm",
"hounskull",
"aventail"
]

armor_body = [
"ringmail",
"platemail",
"plate jacket",
"scalemail",
"curiass",
"scale jacket",
"lamellar armor",
"doublet",
"vest"
]

armor_suffixes = [
" of darkness",
" of light",
" of extended protection",
" of cat-like reflexes",
"","","",""
]

potion_color = [
"white",
"lime green",
"green",
"maroon",
"blood red",
"black",
"chartreuse",
"clear",
"pink",
"brown",
"orange",
"yellow"
]

potion_adjective = [	
"foul-smelling",
"gently-bubbling",
"pleasant",
"greasy",
"oily",
"vibrant",
"volatile"
]

player_first_name = [
"Bilbo",
"Jorg",
"Stiv",
"Eva",
"Hibbo",
"Reginald",
"Pippa",
"Tilda",
"Steve",
"Keldar",
"Aeroth",
"Hodor",
"Labollin",
"Lan",
"Nireal",
"Bane",
"Gunner",
"Mist",
"Aeon",
"Drake",
"Lily",
"Emerald"
]

player_last_name = [
"Hilltopper",
"Falcon",
"Killtaker",
"Beemer",
"Weepins",
"Longfin",
"Waverider",
"Pike",
"Reedcutter",
"Keyendar",
"Bronzeforger",
"Ghoulsmiter",
"Fiendkiller",
"Hottoth",
"Blacksnake",
"Pippins",
"Lancemaster",
"Glitterwise",
"Dusklighter",
"Magusbane",
"Ghostshadow",
"Pineapplehunter",
"Ironmint",
"Nightwish"
]

player_nickname = [
" the white wind",
" of the noble line of Hapsburg", 
" of the black lotus clan",
"", "", "", "", "", "", "", "", "", "", "", "", 
" tamer of the wild hillocks",
" who weeps with uncontrollable fury",
" tallest of the six princes",
" keeper of the eternal flame",
" lord of the seven ponies",
" dancer of the wild rumba",
" dancer in the dark"
]

monster_name = [
"orc",
"goblin",
"ogre",
"vampire",
"lich",
"gnome",
"fiend",
"rodent",
"insectoid",
"kobold",
"bugbear",
"gnoll",
"tiefling",
"troglodyte",
"troll"
]

monster_prefix = [
"huge ",
"stinky ",
"hulking ",
"undead ",
"massive ",
"frost ",
"slime ",
"rock ",
"growling ",
"zombie ",
"blood ",
"dirty ",
"enraged ",
"screaming ",
"glowing ",
"spellbound ",
"crawling ",
"fire breathing ",
"","","","",""
]

monster_suffix = [
" of the deep",
" from the Night-O-Sphere",
" of the Bloodclaw Clan",
" from Mars",
" from the Forbidden Planet",
" of extraordinary size",
" of unusual size",
" of the usual type",
" from the future",
" of the vaults",
" from the Sun Gem Clan",
" from Trenton, NJ",
" of unfathomable horror",
" of eternal pain and sorrow",
"","","","",""
]


### variables ###
rtotal = 1000 # sets the total number of possible rooms


### functions ###
def roll(dice): return randrange(dice) + 1 #create function that returns random number from called range

def coin_toss(): return choice([True, False]) # create function for True/False returns	

def score_up(self, amount): 
	self.score = (self.score + roll(amount) + roll(amount))
	return self.score
	
def weighted_toss(): return choice([True, True, False])



def line(): print "_" * 50

def title():
	print """
  _________                            ____ ___.__   __                 
 /   _____/__ ________   ___________  |    |   \  |_/  |_____________   
 \_____  \|  |  \____ \_/ __ \_  __ \ |    |   /  |\   __\_  __ \__  \  
 /        \  |  /  |_> >  ___/|  | \/ |    |  /|  |_|  |  |  | \// __ \_
/_______  /____/|   __/ \___  >__|    |______/ |____/__|  |__|  (____  /
        \/      |__|        \/                                       \/ 
___________                   ___________.__                            
\_   _____/_ __  ____         \__    ___/|__| _____   ____              
 |    __)|  |  \/    \   ______ |    |   |  |/     \_/ __ \             
 |     \ |  |  /   |  \ /_____/ |    |   |  |  Y Y  \  ___/             
 \___  / |____/|___|  /         |____|   |__|__|_|  /\___  >            
     \/             \/                            \/     \/             
________                          __                                    
\_____  \  __ __   ____   _______/  |_                                  
 /  / \  \|  |  \_/ __ \ /  ___/\   __\                                 
/   \_/.  \  |  /\  ___/ \___ \  |  |                                   
\_____\ \_/____/  \___  >____  > |__|                                   
       \__>           \/     \/                                                            
"""	
def room_preparation(current, previous):
	line()
	print maze[current].index
	print "You enter a %s room. %s" % (maze[current].adjective, maze[current].sentence)
	if maze[current].monster:
		print "There is a %s %s." % (monster_number[current].name, choice(monster_actions))
		print "It has %s hit points, and does %s damage." % (monster_number[current].hp, monster_number[current].damage)
	if maze[current].chest == True and maze[current].monster == True:
		print "You  %s a %schest behind the monster." % (choice(see), chest_number[current].size)
	if maze[current].chest == True and maze[current].monster == False:
		print "You %s a %schest %s." % (choice(see), chest_number[current].size, chest_number[current].where)
	if maze[current].potion == True and maze[current].chest == True:
		print "You %s a %s %s." % (choice(see), potion_number[current].name, potion_number[current].where)
		potion_identifier(current)
	if maze[current].potion == True and maze[current].chest == False:
		print "You %s a %s %s." % (choice(see), potion_number[current].name, potion_number[current].where)
		potion_identifier(current)
	if maze[current].chest == False and maze[current].monster == False and maze[current].potion == False:
		print "%s." % choice(empty_rooms)
	print "what do you do?"
	
	room_choices(current, previous)
	
def player_namer(player):
	print "Let's get started by coming up with a name for your character."
	player.name = "%s %s%s" % (choice(player_first_name), choice(player_last_name), choice(player_nickname))
	print "Based on your biometric readout and unique gaming style, we suggest you name your player \n%s\n" % player.name
	print "What do you think? It's a pretty good name, right?"
	print "1. Yeah, I like it!"
	print "2. It's terrible, but I'll let you try again."
	print "3. You're really bad at naming, let me choose my own."
	player_name_choice = int(raw_input(": "))
	if player_name_choice == 1:
		print "Great, you're one step closer to punching huge monsters in their ugly faces and taking their stuff."
	elif player_name_choice == 2:
		player.name = "%s %s%s" % (choice(player_first_name), choice(player_last_name), choice(player_nickname))
		print "How about %s?" % player.name
	elif player_name_choice == 3:
		print "Well then, impress us with your clever character naming skills."
		player.name = raw_input(": ") 

def player_printout(player):
	print""
	print "%s" % player
	line()
	print "Weapon Equipped: %s" % str(player.arm1)
	print "Head Armor Equipped: %s" % str(player.head)
	print "Body Armor Equipped: %s" % str(player.body)
	print "Hit Points: %s" % player.hp
	print "Damage: %d" % (player.attempt_damage() + int(player.arm1.damage_return()))
	print "Speed: %d" % (player.speed - int(player.head.speed_penalty) + int(player.head.speed_penalty))
	print "Protection: %d" % (int(player.head.protection) + int(player.body.protection))
	print "Current Score: %d" % int(player1.score)
	line()
	print ""
	
		
def player_attributes(player):
	print "%s, let's move on to choosing your attributes." % player.name
	print "Strength effects how much damage you'll do in combat situations."
	print "Dexterity effects how quickly you move."
	print "Luck effects how successful you'll be at a variety of game tasks."
	print "Hit Points will be the total damage you can take before you die."
	print "Now we've consulted our top scientists and they believe that the \nbest attributes for %s would be:" % player.name
	line()
	extra_points = 5
	player.damage = randrange(15,20)
	player.speed = randrange(10,14)
	player.luck = randrange(6,10)
	player.hp = randrange(25,40)
	print "Strength: %d" % player.damage
	print "Dexterity: %d" % player.speed
	print "Luck: %d" % player.luck
	print "Hit Points: %d" % player.hp
	print "Since our scientists are sometimes wrong, we've decided that you'll get %d bonus points\nthat you can add to Strength, Dexterity, Luck, or Hit Points." % extra_points
	while extra_points > 0:
		print "1: Add a point to Strength: %d" % player.damage
		print "2: Add a point to Dexterity: %d" % player.speed
		print "3: Add a point to Luck: %d" % player.luck
		print "4. Add a point to Hit Points: %d" % player.hp
		print "Current extra points: %d" % extra_points
		add_to = int(raw_input("Where would you like to add extra points?\n:"))
		how_many = int(raw_input("How many extra points would you like to add?\n: "))
		if how_many > extra_points:
			how_many = extra_points
		if add_to == 1:
			player.damage += how_many
			print "Added %s to strength." % how_many
			extra_points -= how_many
		elif add_to == 2:
			player.speed += how_many
			print "Added %s to Dexterity." % how_many
			extra_points -= how_many
		elif add_to == 3:
			player.luck += how_many
			print "Added %s to Luck." % how_many
			extra_points -= how_many
		elif add_to == 4:
			player.hp += how_many
			print "Added %s to Hit Points." % how_many
			extra_points -= how_many
		else:
			print "What you just typed... it didn't make any sense."
		
		
def player_equip(player):
	line()
	print "Since you'll be venturing into a very large dungeon to explore, kill things, and earn points" 
	print "you'll probably want some equipment to help keep you alive."
	print "You can wield one weapon at a time and you can equip armor to both your head and body."
	print "Weapons have two attributes, the amount of damage they do and how quickly you can swing them."
	print "Armor also has two attributes, the amount of damage a piece blocks and the dexterity penalty for wearing it."
	line()
	player.arm1 = Weapon()
	player.body = Armor(2)
	player.head = Armor(1)
	print "For Weapons, we'll start you off with a\n%s,\nit does %s damage." % (str(player.arm1), str(player.arm1.damage))
	print "We'll also set you up with some armor for your body; here's a \n%s\n that blocks %s damage." % (str(player.body), str(player.body.protection))
	print "Finally, something to protect your noggin, a\n%s\n that blocks %s damage." % (str(player.head), str(player.head.protection))
	line()

def player_generator(player):
	title()
	print "Welcome to Super Ultra Fun-Time Quest,\nwe're very excited that you've decided to play."
	line()
	player_namer(player)
	line()
	player_attributes(player)
	line()
	player_equip(player)
	print "Looks like you're about ready to hit the dungeons, but"
	print "before you go, there are a few notes on scoring points"
	print "that you'll want to keep in mind."
	print "points are earned for drinking potions, opening chests,"
	print "killing monsters, and exploring new rooms." 
	print "The goal of the game is to earn as many points as possible"
	print "before something kills you."
	raw_input("<Press Enter to Enter the Dungeon>")

		
def random_monster_name(self): # generate a random name combination for monster
	return "%s%s%s" % (choice(monster_prefix), choice(monster_name), choice(monster_suffix))

def chest_content(current): # put item in chest
	inside = randrange(1,6)
	if inside == 1:
		chest_number[current].content_type = "armor"
		chest_number[current].contents = Armor(roll(2))
		if str(chest_number[current].contents.location) == 1:
			chest_number[current].type = "head"
		else:
			chest_number[current].type = "body"
	elif inside == 2:
		chest_number[current].content_type = "weapon"
		chest_number[current].contents = Weapon()
		chest_number[current].type = "arm"
	elif inside == 3:
		chest_number[current].content_type = "trap"
		chest_number[current].contents = "trap"
	elif inside == 4:
		if maze[current].potion:
			inside = 1
		else:	
			chest_number[current].content_type = "potion"
			chest_number[current].contents = potion_number[current]
	else:
		chest_number[current].content_type = "nothing"
		chest_number[current].contents = False
	return chest_number[current].contents	
	
def chest_trap(current):
	dart_damage = randrange(5,10)
	print "A dart springs out from the chest hurting you for %d damage." % dart_damage
	player1.hp -= dart_damage
	if player1.hp <= 0:
		die()
	
		
def chest_lock(current): # roll for unlocking based on character luck stat
	if chest_number[current].locked:
		print "The chest appears to be locked. Do you want to try and open it?"
# enter choices here		
		chest_hard = roll(20)
		luck_chance = roll(player.luck) + player.luck
		if luck_chance >= chest_hard:
			chest_open(current)
		else:
			print "No matter what you try, you can't seem to pick the lock on the chest" 
	else:
		chest_open(current)

def die():
	print "You Died!"
	print "Game Over"
	print "Final Score: %s" % player1.score
	exit()
		
def chest_open(current, previous):
	if chest_number[current].locked:
		print "With a little work, you manage to spring the lock and open the chest" # how to pick up contents
		if chest_number[current].contents == False:
			print "There's nothing in the chest!? Who locks an empty chest?!"
			maze[current].chest = False
			room_preparation(current, previous)
		elif chest_number[current].contents == "trap":
			chest_trap(current)
			
			room_preparation(current, previous)
		else: 	
			print "Inside the chest is %s." % chest_number[current].content_type
			if chest_number[current].content_type == "armor":
				armor_identifier(current)
				print "Do you want to equip the armor?"
			elif chest_number[current].content_type == "weapon":
				weapon_identifier(current)
				print "Do you want to equip the weapon?"
			elif chest_number[current].content_type == "potion":
				potion_identifier(current)
				print "Do you want to drink the potion?"
			chest_pickup(current, previous)
	else:
		print "You open the chest."
		if chest_number[current].contents == "trap":
			chest_trap(current)
			room_preparation(current, previous)
		elif chest_number[current].contents == False:
			print "There's nothing in the chest! I guess that's why it wasn't locked."
			room_preparation(current, previous)
		else:			
			print "Inside the chest is a %s." % chest_number[current].content_type
			if chest_number[current].content_type == "armor":
				armor_identifier(current)
				print "Do you want to equip the armor?"
			elif chest_number[current].content_type == "weapon":
				weapon_identifier(current)
				print "Do you want to equip the weapon?"
			elif chest_number[current].content_type == "potion":
				potion_identifier(current)
				print "Do you want to drink the potion?"
			chest_pickup(current, previous)

			
def armor_identifier(current):
	print "Name: %s" % chest_number[current].contents.name
	if chest_number[current].contents.location == 1:
		location = "head"
	else: 
		location = "body"
	print "Location: %s" % location
	print "Protection: %s" % chest_number[current].contents.protection
	print "Speed Penalty: %s" % chest_number[current].contents.speed_penalty

def weapon_identifier(current):
	print "Name: %s" % chest_number[current].contents.name
	print "Damage: %s" % chest_number[current].contents.damage
	print "Speed: %s" % chest_number[current].contents.speed

def potion_identifier(current):
	print "Name: %s" % potion_number[current].name
	if potion_number[current].label:
		print "Amount: %s" % abs(potion_number[current].health)
	
def chest_pickup(current, previous):
	pickup = int(raw_input("1. Yes\n2. No\n: "))
	if chest_number[current].content_type == "potion" and pickup == 1:
		drink_potion(current, previous)
	if pickup == 1 and chest_number[current].content_type != "potion":
		print "You equip the %s." % chest_number[current].contents
		if chest_number[current].type == "head":
			player1.head = chest_number[current].contents
		elif chest_number[current].type == "body":
			player1.body = chest_number[current].contents
		else:
			player1.arm1 = chest_number[current].contents
		room_preparation(current, previous)
	if pickup == 2:
		print "You leave the %s in the chest." % chest_number[current].contents
	maze[current].chest = False
	room_preparation(current, previous)

	
def damage_calc_player(current):
	player_damage = randrange(player1.attempt_damage() - 7, player1.attempt_damage()) + player1.speed / 2
	monster_protection = (monster_number[current].natural_protection() / 2 )
	damage_dealt = player_damage - monster_protection 
	return damage_dealt
	
def damage_calc_monster(current):
	monster_damage = randrange(((monster_number[current].natural_damage()) - 3), monster_number[current].natural_damage()) + monster_number[current].speed / 2
	player_protection = (player1.armor_protection() / 2)
	damage_taken = monster_damage - player_protection
	return damage_taken
   
def battle(current, previous):
	print "You choose to attack the monster."
	while int(monster_number[current].hp) > 0:
		damage_dealt = damage_calc_player(current)
		damage_taken = damage_calc_monster(current)
		print "You attack the monster for %d damage" % damage_dealt
		print "The monster strikes you for %d damage" % damage_taken
		player1.hp = player1.hp - damage_taken
		if player1.hp <= 0:
			die()
		print "Your current hit points: %d" % player1.hp
		monster_number[current].hp = monster_number[current].hp - damage_dealt
		if monster_number[current].hp < 0: 
			monster_number[current].hp = 0
			print "%s's hit points: %d" % (monster_number[current].name, monster_number[current].hp)
		if monster_number[current].hp == 0:	
			raw_input("You Killed the Monster!\n<Press Enter to Continue>")
			maze[current].monster = False
			if monster_number[current].drop:
				monster_drop(current)
			room_preparation(current, previous)
		else:
			print "%s's hit points: %d" % (monster_number[current].name, monster_number[current].hp)

			
def monster_drop(current):
	drop_item = randrange(1,4)
	if drop_item == 1: 
		monster_number[current].drop = Potion()
		print "The monster dropped a potion!"
		print "Name: %s" % monster_number[current].drop.name
		if monster_number[current].drop.label:
			print "Amount: %s" % abs(monster_number[current].drop.health)
		print "Do you want to drink it?"
		potion_drink = int(raw_input("1. Yes\n2. No\n: "))
		if potion_drink == 1:
			player1.hp += potion_number[current].health
			if potion_number[current].label:
				print "You drink the potion, it adds  %s hit points" % potion_number[current].health
				score_up(player1, 5)
			else:
				print "You drink the potion, uncertain what will happen next."
				score_up(player1, 100)
				if potion_number[current].poison:
					print "You gag, realizing you've just ingested poison. It hurts you for %s hit points." % abs(potion_number[current].health)
				else: 
					print "What luck! The potion heals you for %s hit points." % potion_number[current].health	
			if player1.hp <= 0:
				die()
		else:
			print "You leave the potion alone."
	elif drop_item == 2: 
		monster_number[current].drop = Armor(roll(2))
		print "The monster dropped some armor!"
		print "Name: %s" % monster_number[current].drop.name
		if monster_number[current].drop.location == 1:
			location = "head"
		else:
			location = "body"
		print "Location: %s" % location
		print "Protection: %s" % monster_number[current].drop.protection
		print "Speed Penalty: %s" % monster_number[current].drop.speed_penalty
		equip_armor = int(raw_input("Do you want to equip it?\n1. Yes\n2. No\n: "))
		if equip_armor == 1:
			if location == "head":
				player1.head = monster_number[current].drop
			elif location == "body":
				player1.body = monster_number[current].drop
		else: 
			print "You leave the armor on the ground."
	elif drop_item == 3: 
		monster_number[current].drop = Weapon()
		print "The monster dropped a weapon!"
		print "Name: %s" % monster_number[current].drop.name
		print "Damage: %s" % monster_number[current].drop.damage
		print "Speed: %s" % monster_number[current].drop.speed
		equip_weapon = int(raw_input("Do you want to equip it?\n1. Yes\n2. No\n: "))
		if equip_weapon == 1:
			player1.arm1 = monster_number[current].drop
		else:
			print "You leave the weapon on the ground"
	else:
		print "Danger, Will Robinson"	
	
		
def room_choices(current, previous):
	player_printout(player1)
	print "You have the following choices:"
	options = []
	if maze[current].north:
		options.append("leave towards the north exit")
	if maze[current].east:
		options.append("leave towards the east exit")
	if maze[current].south:
		options.append("leave towards the south exit")
	if maze[current].west:	
		options.append("leave towards west exit")
	if maze[current].monster:
		options.append("attack the monster")
	if maze[current].chest:
		options.append("open the chest")
	if maze[current].potion:
		options.append("drink the potion")
	for item in options:
		print options.index(item) + 1, item
	room_choice = int(raw_input(": "))
	print options[room_choice - 1]
	if (options[room_choice - 1]).find("leave") != -1:
		print "leave room"
		if maze[current].monster:
			getaway_chance = not weighted_toss()
			if getaway_chance:
				print "The monster lunges at you, but you scamper away."
			else:
				print "You try to sneak past the monster, but it notices you and attacks."
				battle(current, previous)
		if (options[room_choice - 1]).find("north") != -1:
			maze[current].exit = "north"
		elif (options[room_choice - 1]).find("east") != -1:
			maze[current].exit = "east"
		elif (options[room_choice - 1]).find("west") != -1:
			maze[current].exit = "west"
		elif (options[room_choice - 1]).find("south") != -1:
			maze[current].exit = "south"
		next = current + 1
		leave_room(current, previous, next)
	elif (options[room_choice - 1]).find("attack") != -1:
		print "attack monster"
		score_up(player1, 10)

		battle(current, previous)
	elif (options[room_choice - 1]).find("open") != -1:
		if maze[current].monster:
			print "As you examine the chest, the monster attacks."
			battle(current, previous)
		print "open chest"
		maze[current].chest = False
		score_up(player1, 10)
		chest_content(current)
		chest_open(current, previous)
	elif (options[room_choice - 1]).find("drink") != -1:
		if maze[current].monster:
			print "You move to pick up the potion, but the monster attacks."
			battle(current, previous)
		print "pick potion"
		score_up(player1, 10)
		drink_potion(current, previous)

def drink_potion(current, previous):
	player1.hp += potion_number[current].health
	if potion_number[current].label:
		print "You drink the potion, it adds  %s hit points" % potion_number[current].health
		score_up(player1, 5)
	else:
		print "You drink the potion, uncertain what will happen next."
		score_up(player1, 100)
		if potion_number[current].poison:
			print "You gag, realizing you've just ingested poison. It hurts you for %s hit points." % abs(potion_number[current].health)
		else: 
			print "What luck! The potion heals you for %s hit points." % potion_number[current].health
	if player1.hp <= 0:
		die()
	maze[current].potion = False
	raw_input("<Press Enter to Continue>")
	room_preparation(current, previous)

def leave_room(current, previous, next):
	global room_pair
	room_pair.append((rooms_visited[current].room_number, maze[current].index))
	score_up(player1, 10)
	print room_pair
	print maze[current].index

	if maze[current].exit == "north":
		maze[next].south = True
		maze[next].index = [(maze[current].index[0] + 1), (maze[current].index[1])]
	elif maze[current].exit == "south":
		maze[next].north = True
		maze[next].index = [(maze[current].index[0] - 1), (maze[current].index[1])]
	elif maze[current].exit == "east":
		maze[next].west = True
		maze[next].index = [(maze[current].index[0]), (maze[current].index[1] + 1)]
	elif maze[current].exit == "west":
		maze[next].east = True
		maze[next].index = [(maze[current].index[0]), (maze[current].index[1] - 1)]
	print maze[next].index
	for value in room_pair:
		if value[1] == maze[next].index:
			room_preparation(value[0], current)
			exit()
	room_preparation(next, current)
		
### classes ###
# create the room class, does not require any attributes when called to create a room
class Room(object):
	def __init__(self, adjective = None, sentence = None, monster = None, potion = None, chest = None, north = None, east = None, south = None, west = None, exit = "", index = [0,0]):
		
		if adjective: self.adjective = adjective
		else: self.adjective = self.random_adjective()
		
		if sentence: self.sentence = sentence
		else: self.sentence = self.random_sentence()
		
		if monster: self.monster = monster
		else: self.monster = coin_toss()
		
		if potion: self.potion = potion
		else: self.potion = not weighted_toss()
		
		if chest: self.chest = chest
		else: self.chest = True
		
		self.north = weighted_toss()
		self.east = weighted_toss()
		self.south = weighted_toss()
		self.west = weighted_toss()
		if self.north == False and self.east == False and self.south == False and self.west == False:
			self.north = True
		
		self.exit = exit
		self.index = index
		
	def random_adjective(self):
		return choice(adjective)
		
	def random_sentence(self):
		return choice(sentence)
		


class Weapon(object): # create the weapon class with two attributes, weapon speed & weapon damage
	def __init__(self):
		self.name = self.weapon_maker()
		self.speed = roll(5)
		self.damage = roll(10)
	def __str__(self):
		return self.name
	def weapon_maker(self):
		return "%s %s %s" % (choice(weapon_prefix), choice(weapon_type), choice(weapon_suffix))
	def damage_return(self):
		return int(self.damage)
		

class Armor(object): # create armor class with two attributes, speed penalty & protection
	def __init__(self, location):
		self.speed_penalty = roll(4)
		self.protection = roll(6)
		self.location = location
		self.name = self.armor_namer()
	def __str__(self):
		return self.name
	def armor_protection(self):
		return int(self.protection)
		
	def armor_namer(self):
		if self.location == 1:
			return "%s%s%s" % (choice(armor_prefixes), choice(armor_head), choice(armor_suffixes))
		else:
			return "%s%s%s" % (choice(armor_prefixes), choice(armor_body), choice(armor_suffixes))



class Potion(object): # create potion class, with one attribute, health given
	def __init__(self):
		self.health = randrange(8, 30)
		self.poison = weighted_toss()
		self.label = not weighted_toss()
		self.where = self.random_where()
		def potion_namer():
			if self.label == False:
				return "%s unmarked potion" % choice(potion_color)
			elif self.poison:
				return "%s %s poisonous potion" % (choice(potion_adjective), choice(potion_color))
			else:
				return "%s healing potion" % choice(potion_color)
		self.name = potion_namer()
		
		def poison_effect():
			if self.poison: self.health = -self.health
		poison_effect()
	def random_where(self):
		return choice(adjective_list_where)
	def __str__(self):
		return self.name
			

class Chest(object): # create chest class, that takes self and contents as initial values
	def __init__(self, contents):
		self.open = False
		self.locked = coin_toss()
		self.contents = contents
		self.type = None
		self.size = self.random_size()
		self.where = self.random_where()
		self.content_type = None
	def __str__(self):
		return self.contents
	def random_size(self):
		return choice(adjective_list_size)
	def random_where(self):
		return choice(adjective_list_where)



class Humanoid(object): 
# create humanoid class, parent of Character & Monster, has five attributes, name, Hit points, base speed, base damage, base protection		
	def __init__(self, name): # hp = None, speed = None, damage = None, protection = None):
		if self.name:
			self.name = name
		else: 
			self.name = "nobody"
		self.hp = None
		self.speed = None
		self.damage = None
		self.protection = None
		if self.hp:
			self.hp = hp
		else:
			self.hp = roll(20)
		if self.speed:
			self.speed = speed
		else:
			self.speed = roll(6)
		if self.damage:
			self.damage = damage
		else:
			self.damage = roll(5)
		if self.protection:
			self.protection = protection
		else:
			self.protection = roll(5)

	


class Character(Humanoid): # create Character class, which adds two arm slots for weapons, and a head and body slot for armor
	def __init__(self):
		super(Humanoid, self).__init__()
		self.name = "nobody"
		self.arm1 = None
		self.head = None
		self.body = None
		self.luck = None
		self.damage = roll(5)
		self.protection = roll(5)
		self.speed = roll(5)
		self.score = 0
	def __str__(self):
		return self.name
	def attempt_damage(self):
		return int(self.damage)
	def armor_protection(self):
		return (self.protection + int(self.head.protection + int(self.body.protection)))


class Monster(Humanoid): # creates Monster class, which adds a slot for weapon drop to Humanoid base, has function that overrides naming from humanoid
	def __init__(self, drop, alive):
		super(Humanoid, self).__init__()
		self.name = random_monster_name(1)
		self.drop = True
		self.alive = True
		self.hp = randrange(10,20)
		self.protection = randrange(4, 9)
		self.damage = randrange(5,10)
		self.speed = roll(20)
	def natural_protection(self):
		return int(self.protection)
	def natural_damage(self):
		return int(self.protection)

class Location(object):
	def __init__(self, room_number):
		self.room_number = room_number
	def __str__(self):
		return self.room_number
	

### Lists ###
chest_number = [] # will contain class instance of chest for each room
monster_number = [] # will contain monster for each room
potion_number = []	# will contain class instance of potion for each room
maze = [] # will contain class instance of each room 
rooms_visited = [] # will contain unique index number to be paired to room.index wne locaiton is visited
room_pair = [] # will contain room number, room index pairs for each room player enters
# create rtotal instances of class room, store the name in the maze array		
for possible_rooms in range(rtotal): maze.append(Room())

for places in range(rtotal): rooms_visited.append(Location(places))


# creates a monster, potion, and chest for each room that has a true value for monster		
for current_room in maze:
	if current_room.monster:
		monster_number.append(Monster(random_monster_name(1), True))
	if current_room.potion:
		potion_number.append(Potion())
	if current_room.chest:
		chest_number.append(Chest(None))


maze[0].index = [0,0] # set initial game coordinate location
player1 = Character() # create player
player_generator(player1) # run player generation code
room_preparation(1, 0)



