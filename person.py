class Person:
  def __init__(self, personName):
    self._name = personName
    self._phone = 0

  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, personName):
    self._name = personName

  @property
  def phone(self):
    return self._phone
  @phone.setter
  def phone(self, personPhone):
    phoneLength = len(str(personPhone))
    if(phoneLength < 8):
      print(self._name + "'s phone " + str(personPhone)+" is too short, make sure you have at least 8 digits")
    else:
      self._phone = personPhone
      rauldata = self._name + " has a phone number " + self._phone
      print("\n"+ rauldata)


raulcv = Person("Raul Louis")
print("Hello "+ raulcv.name +"\n")

print("What is your phone number?")

raulcv.phone = str(input(">"))