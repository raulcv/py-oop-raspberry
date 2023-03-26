import importlib 
# This is the game for move between rooms
roomModule = importlib.import_module("5_roomClass")
characterModule = importlib.import_module("7_characterClass")
itemModule = importlib.import_module("6_itemClass")

from rpginfo import RPGInfo
spookyCastle = RPGInfo("The Spooky Castle")
spookyCastle.welcome()
RPGInfo.info()

RPGInfo.author = "Raul Valeriano\n"
RPGInfo.credits()

kitchen = roomModule.Room("Kitchen")
kitchen.setDescription("A dank and dirty room buzzing with files")

diningHall = roomModule.Room("dining hall")
diningHall.setDescription("A large room with ornate golden decorations on each wall")

ballroom = roomModule.Room("ballroom")
ballroom.setDescription("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

print("There are "+ str(roomModule.Room.numberOfRooms)+ " rooms to explore.")

kitchen.linkRoom(diningHall, "south")
diningHall.linkRoom(kitchen, "north")
diningHall.linkRoom(ballroom, "west")
ballroom.linkRoom(kitchen, "east")

raulcv = characterModule.Enemy("Raul Lois", "A smelly zombie")
raulcv.setConversation("Brrlgrh... rgrhl... brains...")
raulcv.setWeakness("cheese")

diningHall.setCharacter(raulcv)

dino = characterModule.Character("Dino", "A handsome guy!")
dino.setConversation("Hello, Nice to meet you!")
kitchen.setCharacter(dino)

catrina = characterModule.Friend("Catrina", "A friendly skeleton")
catrina.setConversation("Why hello there.")
catrina.setRecieve("Chocolate")
ballroom.setCharacter(catrina)

sculture = itemModule.Item("Zeus sculture")
sculture.setDescription("Zeus height is at least two meters")
ballroom.setItem(sculture)

chocolate = itemModule.Item("Chocolate")
chocolate.setDescription("Colombian Chocolate, it has just 500 calories")
diningHall.setItem(chocolate)
cheese = itemModule.Item("Cheese")
cheese.setDescription("Cheese was eaten by mice")
diningHall.setItem(cheese)

backpack = []

currentRoom = diningHall

dead = False
while dead == False:
  print('\n')
  currentRoom.getDetails()
  inhabitant = currentRoom.getCharacter()
  if inhabitant is not None:
    inhabitant.describe()
  
  itemRoom = currentRoom.getItem()
  if itemRoom is not None:
    itemRoom.describe()

  command = input("> ") # Input from console command
  if command in ["north", "south", "east", "west"]:
    currentRoom = currentRoom.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      raulcv.talk()
  elif command == "fight":
    # You can check whether an object is an instance of a particular
    # class with isinstance() - useful! This code means
    # "If the character is an Enemy"
    if inhabitant is not None and isinstance(inhabitant, characterModule.Enemy):
      print("\nWhat will you fight with?")
      itemNames = []
      totalItems = len(backpack)
      if totalItems  > 0:
        print("you have these things to fight!")
        for item in backpack:
          itemName = item.upper()
          itemNames.append(itemName)
          print(item)
      figthWith = input(" Type > ")
      figthWith = figthWith.upper()

      if figthWith in itemNames:
        if inhabitant.fight(figthWith) == True:
          
          usedItem = backpack.index(figthWith)
          backpack.pop(usedItem)
          counter = characterModule.Enemy.numberOfEnemies
          if counter >= 1:
            # What happens if you win?
            print("Hooray, you won the battle!")
            print("Well done, there is  "+ str(counter) + " enemies left")
          else:
            print("Congratulations, you have vanquished the enemy horde!")
          currentRoom.setCharacter(None)
        else:
          # What happens if you lose?
          print("Oh dear, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
        print("Warning, you cannot have a "+ str(figthWith) + " in your backpack")
    else:
      print("There is no one here to fight with")        

  elif command == "hug":
    if inhabitant is not None:
      if isinstance(inhabitant, characterModule.Enemy):
        print("I wouldn't do that if I were you...")
      else:
        inhabitant.hug()
    else:
      print("There is no one here to hug :(")

  elif command == "gift":
    if inhabitant is not None:
      if isinstance(inhabitant, characterModule.Enemy):
        print("I wouldn't do that if I were you...")
      else:
        print("\nWhat will you give to?")
        giftItem = input()
        inhabitant.gift(giftItem)
    else:
      print("There is no one here to hug :(")

  elif command == "take":
    if currentRoom.item is not None:
      takeTheItem = input("Type Yes or Y to take the item > ")
      takeTheItem = str(takeTheItem).upper()
      if takeTheItem in ["YES", "Y"]:

        backpack.append(itemRoom.getName().upper())
        currentRoom.setItem(None)
        print("\nYou have taken into your backPack ")
        counter = 0
        for item in backpack:
          counter=+1
          print("* "+ str(counter)+ ": "+ item)
      else:
        print("You decided not collect the item ")
    else:
      print("You don't have any items to collect")