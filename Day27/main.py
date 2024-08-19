def create_character():
  name = input("Name your Character: ")
  type = input("Pick Character Type (human/imp/wizard/elf/orc): ")
  
  print("Welcome, " + name +  "!")
  
  return name, type

def gen_health_stats():
  import random
  x = random.randint(1, 6)
  y = random.randint(1, 8)
  health = (x + y)/2 + 10
  return health

def gen_attack_stats():
  import random
  x = random.randint(1, 6)
  y = random.randint(1, 8)
  attack = (x + y)/2 + 12
  return attack

import os, time
addCharacter = "y"
while addCharacter == "y" or addCharacter == 'Y':
  os.system('clear')
  print("Welcome to My Game!")
  print()
  
  name, type = create_character()
  health = gen_health_stats()
  attack = gen_attack_stats()
  print("Your Character is: " + name + " the " + type + ".")
  print("Health: " + str(health))
  print("Attack: " + str(attack))
  print()
  time.sleep(0.5)
  addCharacter = input("Would you like to add another character? (y/n): ")

os.system("clear")
print("Thanks for playing!")