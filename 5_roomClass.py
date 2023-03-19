class Room:
  numberOfRooms = 0 # This is a class variable
  def __init__(self, roomName): #def method define how to look like a class - Self means this object (Room)
    self.name = roomName 
    self.description = None # None measn nothing
    self.linkedRooms = {} #Empty dictionary
    self.character = None
    self.item = None
    Room.numberOfRooms= Room.numberOfRooms + 1

  def setName(self, roomName):
    self.name = roomName
  def getName(self):
    return self.name
  def setDescription(self, roomDescription):
    self.description = roomDescription
  def getDescription(self):
    return self.description
  
  def setCharacter(self, character):
    self.character = character
  def getCharacter(self):
    return self.character

  def setItem(self, item):
    self.item = item
  def getItem(self):
    return self.item

  def describe(self):
    """
    Pirnt on console a string containing the description of the room
    """
    print(self.description)

  def linkRoom(self, roomToLink, direction):
    self.linkedRooms[direction] = roomToLink
    # print( self.name + " linked rooms :" + repr(self.linkedRooms) )
  def getDetails(self):
    print("name: " + self.name)
    print("--------------------")
    print("description: " + self.description+'\n- - - - - - - - ')
    for direction in self.linkedRooms:
      room = self.linkedRooms[direction]
      print( "The "+ room.getName()+ " is "+ direction)
  def move(self, direction):
    if direction in self.linkedRooms:
      return self.linkedRooms[direction]
    else:
      print("You can't go that way")
      return self

pepe = Room("pe")
pepe.describe()