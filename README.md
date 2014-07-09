Super Ultra Fun-Time Quest
=========

Super Ultra Fun-Time Quest is a procedurally generated dungeon-crawler written in Python 2.7 and rendered on the command line.  

This was my first extended programming exercise and as such, features a rather sloppy and haphazard
implementation of classes. 

I took the dungeon crawler intoduced in Python the Hard Way by Zed Shaw and instead of creating a finite dungeon
with defined rooms, I implemented a procedurally generated dungeon with random monster names, room descriptions, items, chests, and potions.  

=========

Lessons learned and things I would do differently

=========

The implementation of classes is weak and inconsistent.  I was a still learning how classes functioned and many of the game's functions should have been built into the classes they relate to. The function player_equip, for example, introduces the armor concept to the player and installs initial armor.  If I were building this again, I would move all the introductory bits into a common function (with an option to skip) and incorporate the armor creation in the initialization of the player class instead of overwriting the initial values. 

I'm proud of the system that allows a player to move from room to room and records where they have been.  This was a particularly challenging bit of code to write and getting it to function properly took a significant amount of trial and error.  I finally resolved the problem by tracking the current and previous room, and storing the rooms visited in a coordinate location paired with a unique key.  the first room is always [[1], [0,0]] the next [[2], [1,0]] if the player moved east or [[2], [0,-1]] if they moved south.  Storing these values in a list allowed me to query the items in the list to determine if the room had been previously visited.  

I learned how to use list iteration to create class instances and then refer back to them.  Generating the random elements in each room was an early challenge and creating all the instances of the room class first, then populating them with chest,  monster, and potion class objects simplified this dramatically.  

