import importlib 
itemModule = importlib.import_module("7_characterClass")

raulcv = itemModule.Enemy("Raul Lois", "A smelly zombie")
raulcv.describe()
# Add some conversation for Raul Lois when he is talked to
raulcv.setConversation("What's up, dude!")
# Trigger a conversation with Raul Lois
raulcv.talk()
# Set a weakness
raulcv.setWeakness("cheese")

# Fight with Raul Lois
print("\nWhat will you fight with?")
figthWith = input()
raulcv.fight(figthWith)