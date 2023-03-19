class Item:
  def __init__(self, itemName):
    self.name = itemName
    self.description = None
  def setName(self, iName):
    self.name = iName
  def getName(self):
    return self.name
  def setDescription(self, iDescription):
    self.description = iDescription
  def getDescription(self):
    return self.description
  
  def describe(self):
    print("\n")
    print("There is a ", self.name + " \n")
    print(self.description + "\n")