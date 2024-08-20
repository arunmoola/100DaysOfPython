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

def print_title():
  os.system('clear')
  print("x BATTLE TIME x")
  print()

def roll_dice():
  import random
  return random.randint(1, 6)

import os, time
print_title()
  
name_1, type_1 = create_character()
health_1 = gen_health_stats()
attack_1 = gen_attack_stats()
print("Player_1 is: " + name_1 + " the " + type_1 + ".")
print("Health: " + str(health_1))
print("Attack: " + str(attack_1))
print()

name_2, type_2 = create_character()
health_2 = gen_health_stats()
attack_2 = gen_attack_stats()
print("Player_2 is: " + name_2 + " the " + type_2 + ".")
print("Health: " + str(health_2))
print("Attack: " + str(attack_2))
print()

if attack_1 >= attack_2:
  gain = attack_1 - attack_2 + 1
else:
  gain = attack_2 - attack_1 + 1  

round = 0
while health_1 > 0 and health_2 > 0:
  time.sleep(5)
  round += 1
  print_title()
  print("Round #:", round)

  roll_1 = roll_dice()
  roll_2 = roll_dice()
  print(name_1 + " rolled a " + str(roll_1) + " and " + name_2 + " rolled a " + str(roll_2) + ".")

  if roll_1 > roll_2:
    print(name_1 + " wins the round!")
    print()
    health_2 -= gain
  elif roll_2 > roll_1:
    print(name_2 + " wins the round!")
    print()
    health_1 -= gain
  else:
    print("It's a tie!")
    print()

  print(name_1 + " the "+ type_1 + " Health: " + str(health_1))
  print(name_2 + " the "+ type_2 + " Health: " + str(health_2))
  print()


time.sleep(1)
print_title()
print(name_1 + " the "+ type_1 + " Health: " + str(health_1))
print(name_2 + " the "+ type_2 + " Health: " + str(health_2))
print()
if health_1 > health_2:
  print(name_1 + " wins the battle in", round, "rounds!")
elif health_2 > health_1:
  print(name_2 + " wins the battle in", round, "rounds!")
else:
  print("Battle Tie!")