class Character:
  # Create a character
  def __init__(self, char_name, charDescription):
    self.name = char_name
    self.description = charDescription
    self.conversation = None
  # Describe this character
  def describe(self):
    print(self.name + " is here!")
    print(self.description)

  # Set what this character will say when talked to
  def setConversation(self, conversation):
    self.conversation = conversation

  # Talk to this character
  def talk(self):
    if self.conversation is not None:
      print("[" + self.name + " says]: " + self.conversation)
    else:
      print(self.name + " doesn't want to talk to you")

  # Fight with this character
  def fight(self, combatItem):
    print(self.name + " doesn't want to fight with you")
    return True


class Enemy(Character):
  numberOfEnemies = 0
  def __init__(self, charName, charDescription):
    super().__init__(
      charName, charDescription
      )  # This means that Enemy is a subclass of Character
    self.weakness = None
    Enemy.numberOfEnemies = Enemy.numberOfEnemies + 1
  def setWeakness(self, weakness):
    self.weakness = weakness

  def getWeakness(self):
    return self.weakness
  def fight(self, combatItem):
    if combatItem == self.weakness.upper():
      print("You fend " + self.name + " off with the "+ combatItem)
      Enemy.numberOfEnemies = Enemy.numberOfEnemies - 1
      return True
    else:
      print(self.name + " crushes you, puny adventurer")
      return False
  def steal(self):
    print("You steal from " + self.name)
    # How will you decide what this character has to steal?

class Friend(Character):
  def __init__(self, friendrName, friendDescription):
    super().__init__(
      friendrName, friendDescription
      )  # This means that Friend is a subclass of Character
    self.recieve = None
    self.feeling = None

  def setRecieve(self, gift):
    self.recieve = gift

  def getRecieve(self):
    return self.recieve

  def gift(self, giftItem):
    if giftItem == self.recieve:
      print(self.name +" said: OMG! " + self.recieve + " This is my favorite gift!")
    else:
      print(self.name + " said you; thanks for your gift!")
  def hug(self):
    print(self.name + " hugs you back!")